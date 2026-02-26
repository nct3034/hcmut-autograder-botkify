import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CPP_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "backend_core", "test_cases"))
TXT_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "backend_core", "expected_outputs"))

os.makedirs(CPP_DIR, exist_ok=True)
os.makedirs(TXT_DIR, exist_ok=True)

test_scenarios = [
    # Test 53: Exception - Bắt ngoại lệ khi gọi playNext hoặc playPrevious trên Playlist rỗng
    (53, """
    Playlist p("Empty Play");
    try {
        p.playNext();
    } catch (const out_of_range& e) {
        cout << "Next Exception: " << e.what() << endl;
    }
    try {
        p.playPrevious();
    } catch (const out_of_range& e) {
        cout << "Prev Exception: " << e.what() << endl;
    }
    """, "Next Exception: Index is invalid!\nPrev Exception: Index is invalid!"),

    # Test 54: Edge case - Playlist chỉ có ĐÚNG 1 bài hát, playNext và playPrevious luôn trả về bài đó
    (54, """
    Playlist p("One Song");
    p.addSong(new Song(1, "Lonely", "Akon", "Alb", 200, 10, "U"));
    cout << "Next: " << p.playNext()->toString() << endl;
    cout << "Next: " << p.playNext()->toString() << endl;
    cout << "Prev: " << p.playPrevious()->toString() << endl;
    cout << "Prev: " << p.playPrevious()->toString() << endl;
    """, "Next: Lonely-Akon\nNext: Lonely-Akon\nPrev: Lonely-Akon\nPrev: Lonely-Akon"),

    # Test 55: Kiểm tra wrap-around (vòng lặp) cơ bản của playNext từ cuối lên đầu
    (55, """
    Playlist p("Play Next Wrap");
    p.addSong(new Song(1, "S1", "A", "A", 10, 10, "U"));
    p.addSong(new Song(2, "S2", "A", "A", 10, 10, "U"));
    p.addSong(new Song(3, "S3", "A", "A", 10, 10, "U"));
    for(int i = 0; i < 4; i++) {
        cout << p.playNext()->toString() << (i == 3 ? "" : " -> ");
    }
    cout << endl;
    """, "S2-A -> S3-A -> S1-A -> S2-A"),

    # Test 56: Kiểm tra wrap-around (vòng lặp) cơ bản của playPrevious từ đầu xuống cuối
    (56, """
    Playlist p("Play Prev Wrap");
    p.addSong(new Song(1, "S1", "A", "A", 10, 10, "U"));
    p.addSong(new Song(2, "S2", "A", "A", 10, 10, "U"));
    p.addSong(new Song(3, "S3", "A", "A", 10, 10, "U"));
    for(int i = 0; i < 4; i++) {
        cout << p.playPrevious()->toString() << (i == 3 ? "" : " -> ");
    }
    cout << endl;
    """, "S3-A -> S2-A -> S1-A -> S3-A"),

    # Test 57: Gọi đan xen playNext và playPrevious để kiểm tra con trỏ vị trí (current state)
    (57, """
    Playlist p("Alternating");
    p.addSong(new Song(1, "S1", "A", "A", 10, 10, "U"));
    p.addSong(new Song(2, "S2", "A", "A", 10, 10, "U"));
    p.addSong(new Song(3, "S3", "A", "A", 10, 10, "U"));
    cout << p.playNext()->toString() << " ";     // Hiện tại đang ở S1 -> Next là S2
    cout << p.playPrevious()->toString() << " "; // Đang ở S2 -> Prev là S1
    cout << p.playPrevious()->toString() << " "; // Đang ở S1 -> Prev là S3
    cout << p.playNext()->toString() << endl;    // Đang ở S3 -> Next là S1
    """, "S2-A S1-A S3-A S1-A"),

    # Test 58: Kiểm tra hành vi sau khi clear() Playlist
    (58, """
    Playlist p("Clear then Play");
    p.addSong(new Song(1, "S1", "A", "A", 10, 10, "U"));
    p.addSong(new Song(2, "S2", "A", "A", 10, 10, "U"));
    p.playNext(); // Qua bài S2
    p.clear();    // Xóa toàn bộ
    try {
        p.playNext(); // Phải ném ngoại lệ vì rỗng
    } catch (const out_of_range& e) {
        cout << "Exception After Clear: " << e.what() << endl;
    }
    """, "Exception After Clear: Index is invalid!"),

    # Test 59: Thêm bài hát mới vào giữa quá trình đang Play
    (59, """
    Playlist p("Add during play");
    p.addSong(new Song(1, "S1", "A", "A", 10, 10, "U"));
    p.addSong(new Song(2, "S2", "A", "A", 10, 10, "U"));
    cout << p.playNext()->toString() << " "; // S2
    // Thêm bài hát S3 vào lúc đang phát S2
    p.addSong(new Song(3, "S3", "A", "A", 10, 10, "U")); 
    cout << p.playNext()->toString() << " "; // Next của S2 bây giờ phải là S3
    cout << p.playNext()->toString() << endl; // Vòng lại S1
    """, "S2-A S3-A S1-A"),

    # Test 60: Gọi playPrevious ngay lần đầu tiên (từ vị trí 0 vòng xuống cuối)
    (60, """
    Playlist p("Prev at start");
    p.addSong(new Song(1, "S1", "A", "A", 10, 10, "U"));
    p.addSong(new Song(2, "S2", "A", "A", 10, 10, "U"));
    p.addSong(new Song(3, "S3", "A", "A", 10, 10, "U"));
    p.addSong(new Song(4, "S4", "A", "A", 10, 10, "U"));
    cout << p.playPrevious()->toString() << endl; // S1 vòng xuống S4
    """, "S4-A"),

    # Test 61: Stress test việc chạy tới / lùi vòng tròn liên tục 100 lần (kiểm tra rò rỉ bộ nhớ hoặc lỗi vòng lặp)
    (61, """
    Playlist p("Stress Next/Prev");
    for(int i = 0; i < 5; i++) {
        p.addSong(new Song(i, "S" + to_string(i), "A", "A", 10, 10, "U"));
    }
    for(int i = 0; i < 100; i++) p.playNext();
    // 100 chia hết cho 5, vị trí hiện tại lại quay về 0
    cout << "After 100 next: " << p.playNext()->toString() << endl; // Nhảy lên 1
    
    for(int i = 0; i < 100; i++) p.playPrevious();
    // 100 lần lùi lại quay về đúng vị trí 1
    cout << "After 100 prev: " << p.playPrevious()->toString() << endl; // Lùi về 0
    """, "After 100 next: S1-A\nAfter 100 prev: S0-A"),

    # Test 62: Edge case - Danh sách có đúng 2 bài hát, đan xen liên tục
    (62, """
    Playlist p("Size 2 Edge");
    p.addSong(new Song(1, "A", "Art", "A", 10, 10, "U"));
    p.addSong(new Song(2, "B", "Art", "A", 10, 10, "U"));
    cout << p.playNext()->toString() << " ";     // B
    cout << p.playNext()->toString() << " ";     // A
    cout << p.playPrevious()->toString() << " "; // B
    cout << p.playPrevious()->toString() << endl;// A
    """, "B-Art A-Art B-Art A-Art")
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
    print("✅ Đã tạo xong test 53 - 62 cho playNext() và playPrevious()!")

if __name__ == "__main__":
    generate()