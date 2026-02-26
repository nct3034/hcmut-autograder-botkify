import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CPP_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "backend_core", "test_cases"))
TXT_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "backend_core", "expected_outputs"))

os.makedirs(CPP_DIR, exist_ok=True)
os.makedirs(TXT_DIR, exist_ok=True)

test_scenarios = [
    # Test 83: Chuỗi duration tăng dần đều.
    (83, """
    Playlist p("T83");
    p.addSong(new Song(1, "A", "A", "A", 10, 10, "U"));
    p.addSong(new Song(2, "B", "A", "A", 20, 10, "U"));
    p.addSong(new Song(3, "C", "A", "A", 30, 10, "U"));
    cout << "Test 83: ";
    p.playRandom(0);
    cout << endl;
    """, "Test 83: A-A,B-A,C-A\n"),

    # Test 84: Chỉ có đúng một bài có duration lớn hơn và nằm phía sau.
    (84, """
    Playlist p("T84");
    p.addSong(new Song(1, "A", "A", "A", 10, 10, "U"));
    p.addSong(new Song(2, "B", "A", "A", 10, 10, "U"));
    p.addSong(new Song(3, "C", "A", "A", 50, 10, "U"));
    p.addSong(new Song(4, "D", "A", "A", 10, 10, "U"));
    cout << "Test 84: ";
    p.playRandom(0); // Từ A(10) sẽ tìm thấy C(50)
    cout << endl;
    """, "Test 84: A-A,C-A\n"),

    # Test 85: Chỉ có đúng một bài có duration lớn hơn và nằm phía trước (bên trái).
    (85, """
    Playlist p("T85");
    p.addSong(new Song(1, "A", "A", "A", 10, 10, "U"));
    p.addSong(new Song(2, "B", "A", "A", 50, 10, "U"));
    p.addSong(new Song(3, "C", "A", "A", 10, 10, "U"));
    p.addSong(new Song(4, "D", "A", "A", 10, 10, "U"));
    cout << "Test 85: ";
    p.playRandom(3); // Từ D(10) sẽ phải lùi về tìm thấy B(50)
    cout << endl;
    """, "Test 85: D-A,B-A\n"),

    # Test 86: Tất cả bài hát có cùng duration (không có bài nào lớn hơn).
    (86, """
    Playlist p("T86");
    p.addSong(new Song(1, "A", "A", "A", 20, 10, "U"));
    p.addSong(new Song(2, "B", "A", "A", 20, 10, "U"));
    p.addSong(new Song(3, "C", "A", "A", 20, 10, "U"));
    cout << "Test 86: ";
    p.playRandom(1);
    cout << endl;
    """, "Test 86: B-A\n"),

    # Test 87: Edge case - Playlist chỉ có đúng 1 bài hát.
    (87, """
    Playlist p("T87");
    p.addSong(new Song(1, "A", "A", "A", 10, 10, "U"));
    cout << "Test 87: ";
    p.playRandom(0);
    cout << endl;
    """, "Test 87: A-A\n"),

    # Test 88: Hai bài lớn hơn nằm ở hai phía, nhưng khoảng cách lệch nhau rõ ràng để tránh hòa.
    # Start ở B(index 1). A(index 0) có dur=20 (dist 1). D(index 3) có dur=30 (dist 2). C phải chọn A.
    (88, """
    Playlist p("T88");
    p.addSong(new Song(0, "A", "A", "A", 20, 10, "U"));
    p.addSong(new Song(1, "B", "A", "A", 10, 10, "U"));
    p.addSong(new Song(2, "C", "A", "A", 10, 10, "U"));
    p.addSong(new Song(3, "D", "A", "A", 30, 10, "U"));
    cout << "Test 88: ";
    p.playRandom(1);
    cout << endl;
    """, "Test 88: B-A,A-A,D-A\n"),

    # Test 89: Bước nhảy xa, bỏ qua các bài có duration thấp hơn.
    (89, """
    Playlist p("T89");
    p.addSong(new Song(0, "A", "A", "A", 100, 10, "U"));
    p.addSong(new Song(1, "B", "A", "A", 1, 10, "U"));
    p.addSong(new Song(2, "C", "A", "A", 5, 10, "U"));
    p.addSong(new Song(3, "D", "A", "A", 2, 10, "U"));
    p.addSong(new Song(4, "E", "A", "A", 1, 10, "U"));
    cout << "Test 89: ";
    p.playRandom(2); // C(5) -> A(100)
    cout << endl;
    """, "Test 89: C-A,A-A\n"),

    # Test 90: Start ở cuối danh sách, kiểm tra logic chỉ tìm lùi.
    (90, """
    Playlist p("T90");
    p.addSong(new Song(0, "A", "A", "A", 40, 10, "U"));
    p.addSong(new Song(1, "B", "A", "A", 10, 10, "U"));
    p.addSong(new Song(2, "C", "A", "A", 10, 10, "U"));
    cout << "Test 90: ";
    p.playRandom(2); // C(10) -> A(40)
    cout << endl;
    """, "Test 90: C-A,A-A\n"),

    # Test 91: Các duration tăng dần nhưng nằm xen kẽ để kiểm tra tính đúng đắn của việc lan rộng.
    (91, """
    Playlist p("T91");
    p.addSong(new Song(0, "A", "A", "A", 30, 10, "U"));
    p.addSong(new Song(1, "B", "A", "A", 10, 10, "U"));
    p.addSong(new Song(2, "C", "A", "A", 20, 10, "U"));
    cout << "Test 91: ";
    p.playRandom(1); // B(10) -> C(20) [dist 1] -> A(30) [dist 2 từ C]
    cout << endl;
    """, "Test 91: B-A,C-A,A-A\n"),

    # Test 92: Start ở index lớn, không có bài nào bên phải thỏa mãn, buộc phải lấy bên trái.
    (92, """
    Playlist p("T92");
    p.addSong(new Song(0, "A", "A", "A", 100, 10, "U"));
    p.addSong(new Song(1, "B", "A", "A", 10, 10, "U"));
    p.addSong(new Song(2, "C", "A", "A", 10, 10, "U"));
    p.addSong(new Song(3, "D", "A", "A", 50, 10, "U"));
    cout << "Test 92: ";
    p.playRandom(3); // D(50) -> A(100)
    cout << endl;
    """, "Test 92: D-A,A-A\n")
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
    print("✅ Đã tạo xong test 83 - 92 cho playRandom()!")

if __name__ == "__main__":
    generate()