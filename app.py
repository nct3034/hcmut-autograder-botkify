from flask import Flask, render_template, request, jsonify, Response
import subprocess
import os
import shutil
import uuid
import glob
import json

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
BACKEND_CORE = 'backend_core'

# Định nghĩa rõ ràng 3 thư mục lõi
PROCESS_DIR = os.path.join(BACKEND_CORE, 'process')
TEST_CASES_DIR = os.path.join(BACKEND_CORE, 'test_cases')
EXPECTED_DIR = os.path.join(BACKEND_CORE, 'expected_outputs')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/submit', methods=['POST'])
def submit():
    if 'files' not in request.files:
        return jsonify({"error": "Không tìm thấy file!"}), 400
    
    uploaded_files = request.files.getlist('files')
    if len(uploaded_files) == 0 or uploaded_files[0].filename == '':
        return jsonify({"error": "Bạn chưa chọn file nào!"}), 400

    session_id = str(uuid.uuid4()) 
    work_dir = os.path.abspath(os.path.join(UPLOAD_FOLDER, session_id))
    os.makedirs(work_dir, exist_ok=True)

    # 1. Lưu file sinh viên nộp
    for f in uploaded_files:
        f.save(os.path.join(work_dir, f.filename))

    # 2. Copy file hệ thống TỪ THƯ MỤC process/
    main_h_path = os.path.join(PROCESS_DIR, 'main.h')
    utils_h_path = os.path.join(PROCESS_DIR, 'utils.h')
    if os.path.exists(main_h_path): shutil.copy(main_h_path, work_dir)
    if os.path.exists(utils_h_path): shutil.copy(utils_h_path, work_dir)

    test_files = sorted(glob.glob(os.path.join(TEST_CASES_DIR, '*.cpp')))
    if not test_files:
        return jsonify({"error": "Hệ thống chưa có bài test nào!"}), 400

    # Đọc sẵn file Template từ thư mục process/
    template_path = os.path.join(PROCESS_DIR, 'main_template.cpp')
    main_template = ""
    if os.path.exists(template_path):
        with open(template_path, 'r', encoding='utf-8') as f:
            main_template = f.read()
    else:
        # Nếu chẳng may mất file, dùng chuỗi dự phòng
        main_template = '#include "main.h"\n#include "Playlist.h"\n___TEST_CODE___\nint main() { ___TEST_NAME___(); return 0; }'

    # 3. Hàm Generator để Stream dữ liệu thời gian thực
    def generate_results():
        try:
            total_tests = len(test_files)
            yield json.dumps({"type": "start", "total": total_tests}) + "\n"

            for test_cpp_path in test_files:
                test_id = os.path.splitext(os.path.basename(test_cpp_path))[0]
                
                with open(test_cpp_path, 'r', encoding='utf-8') as tc_file:
                    test_code = tc_file.read().strip()

                txt_path = os.path.join(EXPECTED_DIR, f"{test_id}.txt")
                expected_out = ""
                if os.path.exists(txt_path):
                    with open(txt_path, 'r', encoding='utf-8') as tf:
                        expected_out = tf.read().strip()
                else:
                    expected_out = "[LỖI] Không tìm thấy đáp án"

                # 4. Sử dụng main_template.cpp để bọc code
                wrapped_code = main_template.replace('___TEST_CODE___', test_code).replace('___TEST_NAME___', test_id)
                with open(os.path.join(work_dir, 'main.cpp'), 'w', encoding='utf-8') as f:
                    f.write(wrapped_code)

                # Biên dịch
                exec_name = "exec_test.exe"
                compile_cmd = ["g++", "main.cpp", "Playlist.cpp", "-std=c++17", "-o", exec_name]
                compile_process = subprocess.run(compile_cmd, cwd=work_dir, capture_output=True, text=True)
                
                if compile_process.returncode != 0:
                    result = {
                        "type": "result", "test_id": test_id, "test_code": test_code, 
                        "expected": expected_out, "got": compile_process.stderr, "status": "COMPILE ERROR"
                    }
                    yield json.dumps(result) + "\n"
                    continue 

                # Chạy File
                exec_path = os.path.join(work_dir, exec_name)
                try:
                    run_process = subprocess.run([exec_path], cwd=work_dir, capture_output=True, text=True, timeout=3)
                    got_out = run_process.stdout.strip()
                    is_passed = (got_out == expected_out)
                    
                    result = {
                        "type": "result", "test_id": test_id, "test_code": test_code, 
                        "expected": expected_out, "got": got_out, "status": "PASSED" if is_passed else "FAILED"
                    }
                except subprocess.TimeoutExpired:
                    result = {
                        "type": "result", "test_id": test_id, "test_code": test_code, 
                        "expected": expected_out, "got": "Quá thời gian (TLE)", "status": "FAILED"
                    }
                
                yield json.dumps(result) + "\n"

            yield json.dumps({"type": "done"}) + "\n"

        finally:
            if os.path.exists(work_dir):
                shutil.rmtree(work_dir)

    return Response(generate_results(), mimetype='application/x-ndjson')

if __name__ == '__main__':
    app.run(debug=True, port=5000)