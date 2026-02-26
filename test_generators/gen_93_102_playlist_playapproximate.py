import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CPP_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "backend_core", "test_cases"))
TXT_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "backend_core", "expected_outputs"))

os.makedirs(CPP_DIR, exist_ok=True)
os.makedirs(TXT_DIR, exist_ok=True)

test_scenarios = [
    # Test 93: Khớp hoàn toàn với Example 3.5 trong Spec (Duration: {50, 60, 30, 90, 100}, step = 1)
    # Lộ trình: 50 -> 60 -> 90 -> 100. Diff = 10 + 30 + 10 = 50.
    (93, """
    Playlist p("T93");
    p.addSong(new Song(1, "A", "A", "A", 50, 0, "A"));
    p.addSong(new Song(2, "B", "B", "B", 60, 0, "B"));
    p.addSong(new Song(3, "C", "C", "C", 30, 0, "C"));
    p.addSong(new Song(4, "D", "D", "D", 90, 0, "D"));
    p.addSong(new Song(5, "E", "E", "E", 100, 0, "E"));
    cout << "Test 93: " << p.playApproximate(1) << endl;
    """, "Test 93: 50"),

    # Test 94: step = 0 (Không được phép bỏ qua bài hát nào)
    # Duration: {10, 20, 50, 40} -> Lộ trình bắt buộc: 10 -> 20 -> 50 -> 40.
    # Diff = 10 + 30 + 10 = 50.
    (94, """
    Playlist p("T94");
    p.addSong(new Song(1, "A", "A", "A", 10, 0, "A"));
    p.addSong(new Song(2, "B", "B", "B", 20, 0, "B"));
    p.addSong(new Song(3, "C", "C", "C", 50, 0, "C"));
    p.addSong(new Song(4, "D", "D", "D", 40, 0, "D"));
    cout << "Test 94: " << p.playApproximate(0) << endl;
    """, "Test 94: 50"),

    # Test 95: step lớn, đủ để nhảy thẳng từ đầu đến cuối danh sách (bỏ qua toàn bộ phần giữa)
    # Duration: {10, 100, 100, 20}, step = 2.
    # Lộ trình: 10 -> 20 (bỏ qua 2 bài hát 100). Diff = 10.
    (95, """
    Playlist p("T95");
    p.addSong(new Song(1, "A", "A", "A", 10, 0, "A"));
    p.addSong(new Song(2, "B", "B", "B", 100, 0, "B"));
    p.addSong(new Song(3, "C", "C", "C", 100, 0, "C"));
    p.addSong(new Song(4, "D", "D", "D", 20, 0, "D"));
    cout << "Test 95: " << p.playApproximate(2) << endl;
    """, "Test 95: 10"),

    # Test 96: Tất cả bài hát đều có cùng duration
    # Duration: {50, 50, 50, 50}, step = 1.
    # Diff phải luôn bằng 0 dù đi đường nào.
    (96, """
    Playlist p("T96");
    p.addSong(new Song(1, "A", "A", "A", 50, 0, "A"));
    p.addSong(new Song(2, "B", "B", "B", 50, 0, "B"));
    p.addSong(new Song(3, "C", "C", "C", 50, 0, "C"));
    p.addSong(new Song(4, "D", "D", "D", 50, 0, "D"));
    cout << "Test 96: " << p.playApproximate(1) << endl;
    """, "Test 96: 0"),

    # Test 97: Chứa 1 bài hát có thời lượng cực lớn (nhiễu) nằm chen ngang, ép nhảy qua.
    # Duration: {0, 10, 20, 100, 30, 40}, step = 1.
    # Lộ trình tối ưu: 0 -> 10 -> 20 -> 30 -> 40. Diff = 40.
    (97, """
    Playlist p("T97");
    p.addSong(new Song(1, "A", "A", "A", 0, 0, "A"));
    p.addSong(new Song(2, "B", "B", "B", 10, 0, "B"));
    p.addSong(new Song(3, "C", "C", "C", 20, 0, "C"));
    p.addSong(new Song(4, "D", "D", "D", 100, 0, "D"));
    p.addSong(new Song(5, "E", "E", "E", 30, 0, "E"));
    p.addSong(new Song(6, "F", "F", "F", 40, 0, "F"));
    cout << "Test 97: " << p.playApproximate(1) << endl;
    """, "Test 97: 40"),

    # Test 98: Dữ liệu Zigzag để kiểm tra DP.
    # Duration: {10, 100, 20, 100, 30}, step = 1.
    # Lộ trình tối ưu: 10 -> 20 -> 30. Diff = 20.
    (98, """
    Playlist p("T98");
    p.addSong(new Song(1, "A", "A", "A", 10, 0, "A"));
    p.addSong(new Song(2, "B", "B", "B", 100, 0, "B"));
    p.addSong(new Song(3, "C", "C", "C", 20, 0, "C"));
    p.addSong(new Song(4, "D", "D", "D", 100, 0, "D"));
    p.addSong(new Song(5, "E", "E", "E", 30, 0, "E"));
    cout << "Test 98: " << p.playApproximate(1) << endl;
    """, "Test 98: 20"),

    # Test 99: Dữ liệu yêu cầu nhảy step = 2 mới tìm được đường tối ưu.
    # Duration: {0, 100, 100, 10, 100, 100, 20}, step = 2.
    # Lộ trình tối ưu: 0 -> 10 -> 20. Diff = 20.
    (99, """
    Playlist p("T99");
    p.addSong(new Song(1, "A", "A", "A", 0, 0, "A"));
    p.addSong(new Song(2, "B", "B", "B", 100, 0, "B"));
    p.addSong(new Song(3, "C", "C", "C", 100, 0, "C"));
    p.addSong(new Song(4, "D", "D", "D", 10, 0, "D"));
    p.addSong(new Song(5, "E", "E", "E", 100, 0, "E"));
    p.addSong(new Song(6, "F", "F", "F", 100, 0, "F"));
    p.addSong(new Song(7, "G", "G", "G", 20, 0, "G"));
    cout << "Test 99: " << p.playApproximate(2) << endl;
    """, "Test 99: 20"),

    # Test 100: Duration giảm dần, nhưng việc nhảy step làm giảm tổng chênh lệch đáng kể.
    # Duration: {100, 10, 80, 10, 60}, step = 1.
    # Lộ trình: 100 -> 80 -> 60. Diff = 20 + 20 = 40.
    (100, """
    Playlist p("T100");
    p.addSong(new Song(1, "A", "A", "A", 100, 0, "A"));
    p.addSong(new Song(2, "B", "B", "B", 10, 0, "B"));
    p.addSong(new Song(3, "C", "C", "C", 80, 0, "C"));
    p.addSong(new Song(4, "D", "D", "D", 10, 0, "D"));
    p.addSong(new Song(5, "E", "E", "E", 60, 0, "E"));
    cout << "Test 100: " << p.playApproximate(1) << endl;
    """, "Test 100: 40"),

    # Test 101: Edge case - Danh sách chỉ có đúng 2 bài hát. Step có lớn đến mấy cũng chỉ nhảy được 1 bước (diff của 2 phần tử).
    # Duration: {10, 50}, step = 10.
    # Diff = 40.
    (101, """
    Playlist p("T101");
    p.addSong(new Song(1, "A", "A", "A", 10, 0, "A"));
    p.addSong(new Song(2, "B", "B", "B", 50, 0, "B"));
    cout << "Test 101: " << p.playApproximate(10) << endl;
    """, "Test 101: 40"),

    # Test 102: step bằng số lượng bỏ qua vừa khít để đi thẳng từ đầu đến cuối mà không vi phạm.
    # Duration: {1, 9, 9, 9, 5}, step = 3.
    # Bỏ qua đúng 3 bài hát ở giữa. Lộ trình: 1 -> 5. Diff = 4.
    (102, """
    Playlist p("T102");
    p.addSong(new Song(1, "A", "A", "A", 1, 0, "A"));
    p.addSong(new Song(2, "B", "B", "B", 9, 0, "B"));
    p.addSong(new Song(3, "C", "C", "C", 9, 0, "C"));
    p.addSong(new Song(4, "D", "D", "D", 9, 0, "D"));
    p.addSong(new Song(5, "E", "E", "E", 5, 0, "E"));
    cout << "Test 102: " << p.playApproximate(3) << endl;
    """, "Test 102: 4")
]

def generate():
    for num, code, expected in test_scenarios:
        cpp_fn = f"test_{num:03d}.cpp"
        txt_fn = f"test_{num:03d}.txt"
        with open(os.path.join(CPP_DIR, cpp_fn), "w", encoding="utf-8") as f:
            f.write(f"void test_{num:03d}() {{\n")
            f.write(code.strip("\n")) 
            f.write("\n}\n")
        with open(os.path.join(TXT_DIR, txt_fn), "w", encoding="utf-8") as f:
            f.write(expected)
    print("✅ Đã tạo xong test 93 - 102 cho playApproximate(int step)!")

if __name__ == "__main__":
    generate()