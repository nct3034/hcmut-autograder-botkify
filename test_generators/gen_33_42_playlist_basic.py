import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CPP_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "backend_core", "test_cases"))
TXT_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "backend_core", "expected_outputs"))

os.makedirs(CPP_DIR, exist_ok=True)
os.makedirs(TXT_DIR, exist_ok=True)

test_scenarios = [
    # Test 33: Khởi tạo Playlist, kiểm tra trạng thái rỗng và size ban đầu
    (33, """
    Playlist p("My Chill Playlist");
    cout << "Size: " << p.size() << " | Empty: " << (p.empty() ? "Yes" : "No") << endl;
    """, "Size: 0 | Empty: Yes"),

    # Test 34: Thêm 1 bài hát, kiểm tra size và trạng thái rỗng thay đổi
    (34, """
    Playlist p("Hits 2026");
    p.addSong(new Song(1, "Don't Start Now", "Dua Lipa", "Future Nostalgia", 183, 850, "url"));
    cout << "Size: " << p.size() << " | Empty: " << (p.empty() ? "Yes" : "No") << endl;
    """, "Size: 1 | Empty: No"),

    # Test 35: Thêm nhiều bài hát liên tiếp và kiểm tra size tăng dần
    (35, """
    Playlist p("Kpop");
    p.addSong(new Song(1, "Ditto", "NewJeans", "OMG", 185, 900, "url1"));
    p.addSong(new Song(2, "Hype Boy", "NewJeans", "New Jeans", 179, 950, "url2"));
    p.addSong(new Song(3, "Super Shy", "NewJeans", "Get Up", 154, 920, "url3"));
    cout << "Final Size: " << p.size() << endl;
    """, "Final Size: 3"),

    # Test 36: getSong cơ bản ở các vị trí khác nhau (đầu, giữa, cuối)
    (36, """
    Playlist p("Vpop");
    p.addSong(new Song(10, "Waiting For You", "MONO", "22", 265, 800, "u"));
    p.addSong(new Song(11, "See Tinh", "Hoang Thuy Linh", "LINK", 195, 850, "u"));
    p.addSong(new Song(12, "Ngay Mai Nguoi Ta Lay Chong", "Thanh Dat", "Single", 310, 750, "u"));
    cout << "Index 0: " << p.getSong(0)->toString() << endl;
    cout << "Index 2: " << p.getSong(2)->toString() << endl;
    cout << "Index 1: " << p.getSong(1)->toString() << endl;
    """, "Index 0: Waiting For You-MONO\nIndex 2: Ngay Mai Nguoi Ta Lay Chong-Thanh Dat\nIndex 1: See Tinh-Hoang Thuy Linh"),

    # Test 37: getSong ném ngoại lệ out_of_range khi index >= size
    (37, """
    Playlist p("Error Handling");
    p.addSong(new Song(1, "A", "B", "C", 10, 10, "U"));
    try {
        p.getSong(1); // Size là 1, index hợp lệ chỉ là 0
    } catch (const out_of_range& e) {
        cout << "Caught Exception: " << e.what() << endl;
    }
    """, "Caught Exception: Index is invalid!"),

    # Test 38: getSong ném ngoại lệ out_of_range khi index < 0
    (38, """
    Playlist p("Error Handling Negative");
    p.addSong(new Song(1, "A", "B", "C", 10, 10, "U"));
    try {
        p.getSong(-5);
    } catch (const out_of_range& e) {
        cout << "Caught Exception: " << e.what() << endl;
    }
    """, "Caught Exception: Index is invalid!"),

    # Test 39: clear() cơ bản, kiểm tra size và trạng thái empty sau khi gọi
    (39, """
    Playlist p("To Clear");
    p.addSong(new Song(1, "Song A", "Artist A", "Album A", 100, 10, "url"));
    p.addSong(new Song(2, "Song B", "Artist B", "Album B", 200, 20, "url"));
    p.clear();
    cout << "Size after clear: " << p.size() << " | Empty: " << (p.empty() ? "Yes" : "No") << endl;
    """, "Size after clear: 0 | Empty: Yes"),

    # Test 40: clear() trên một Playlist vốn đã rỗng (không gây lỗi)
    (40, """
    Playlist p("Empty Clear");
    p.clear();
    cout << "Size: " << p.size() << " | Empty: " << (p.empty() ? "Yes" : "No") << endl;
    """, "Size: 0 | Empty: Yes"),

    # Test 41: Thêm bài hát sau khi clear() để đảm bảo cấu trúc list vẫn hoạt động tốt
    (41, """
    Playlist p("Add After Clear");
    p.addSong(new Song(1, "Old Song", "A", "B", 100, 50, "U"));
    p.clear();
    p.addSong(new Song(2, "New Song", "C", "D", 200, 60, "U"));
    cout << "Size: " << p.size() << " | First song: " << p.getSong(0)->toString() << endl;
    """, "Size: 1 | First song: New Song-C"),

    # Test 42: Thêm số lượng lớn bài hát (1000 bài) để kiểm tra hiệu năng cơ bản và tính toàn vẹn
    (42, """
    Playlist p("Large Playlist");
    for(int i = 0; i < 1000; i++) {
        p.addSong(new Song(i, "Title", "Artist", "Album", i, i % 1000, "url"));
    }
    cout << "Size: " << p.size() << " | getSong(500) ID: " << p.getSong(500)->getID() << endl;
    p.clear();
    cout << "Size after clear: " << p.size() << endl;
    """, "Size: 1000 | getSong(500) ID: 500\nSize after clear: 0")
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
    print("✅ Đã tạo xong test 33 - 42 cho các hàm cơ bản của Playlist!")

if __name__ == "__main__":
    generate()