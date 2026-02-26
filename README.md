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

## 3. Tạo ra testcase mẫu

Mở Terminal tích hợp trong VS Code (phím tắt Ctrl + `).

Chạy lệnh sau để tự động tạo 10 testcase và file đáp án mẫu:

```

python test_generators/gen_01_10_basic.py
```

Trong folder test_generators có một vài chương trình có thể tạo vài testcase mẫu.
Cú pháp:

```
python test_generators/tên_chương_trình
```

Nếu bạn muốn cài đặt toàn bộ testcase

```
python test_generators/gen_01_10_basic.py
python test_generators/gen_11_22_linkedlist.py
python test_generators/gen_23_32_song.py
python test_generators/gen_33_42_playlist_basic.py
python test_generators/gen_43_52_playlist_removesong.py
python test_generators/gen_53_62_playlist_play.py
python test_generators/gen_63_72_playlist_gettotalscore.py
```

## 4. Cách thêm testcase và expected để kiểm tra

Nếu bạn muốn tự thêm một test case riêng lẻ để kiểm tra lỗi cụ thể:

Bước 1 (Code): Tạo file test_xxx.cpp trong backend_core/test_cases/.

Nội dung: Chỉ chứa duy nhất một hàm void (VD: void test_xxx() { ... }).

Bước 2 (Đáp án): Tạo file test_xxx.txt trong backend_core/expected_outputs/.

Nội dung: Chứa kết quả chính xác mà chương trình cần in ra màn hình.

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
