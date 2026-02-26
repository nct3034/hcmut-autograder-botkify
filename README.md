# HCMUT AutoGrader - BotKify

## 1. Cài đặt Python và Flask để chạy

- Tải và cài đặt Python từ trang chủ (python.org). **Lưu ý:** Phải tích chọn ô **"Add python.exe to PATH"** trong quá trình cài đặt.
- Mở Terminal (hoặc CMD) và chạy lệnh sau để cài Flask:

  ```cmd
  pip install flask
  ```

## 2. Mở VS Code

Mở phần mềm Visual Studio Code.

Chọn File > Open Folder và mở thư mục chứa mã nguồn của dự án này.

## 3. Tạo ra 10 testcase mẫu ban đầu

Mở Terminal tích hợp trong VS Code (phím tắt Ctrl + `).

Chạy lệnh sau để tự động tạo 10 testcase và file đáp án mẫu:

```

python generate_tests.py
```

## 4. Cách thêm testcase và expected để kiểm tra

Thêm Testcase: Tạo file test_xxx.cpp trong thư mục backend_core/test_cases/. File này chỉ chứa duy nhất một hàm void (VD: void test_xxx() { ... }).

Thêm Expected: Tạo file test_xxx.txt chứa kết quả in ra màn hình tương ứng và đặt trong thư mục backend_core/expected_outputs/.

## 5. Cách chạy chương trình

Tại Terminal của VS Code, khởi động server bằng lệnh:

```

python app.py
```

Chương trình chạy thành công khi Terminal hiện dòng chữ Running on http://127.0.0.1:5000.

## 6. Mở chương trình và nộp bài

Mở trình duyệt Web (Chrome, Edge, Safari,...) và truy cập vào địa chỉ: http://127.0.0.1:5000

Kéo thả các file bài làm (VD: BotkifyLinkedList.h, Playlist.h, Playlist.cpp) vào khu vực nộp bài.

Bấm nút "Nộp Bài & Chấm Điểm" và xem kết quả.
