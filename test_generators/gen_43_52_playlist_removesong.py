import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CPP_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "backend_core", "test_cases"))
TXT_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "backend_core", "expected_outputs"))

os.makedirs(CPP_DIR, exist_ok=True)
os.makedirs(TXT_DIR, exist_ok=True)

test_scenarios = [
    # Test 43: Xóa bài hát ở vị trí đầu tiên (index = 0)
    (43, """
    Playlist p("Test 43");
    p.addSong(new Song(1, "A", "ArtA", "Alb", 100, 10, "U"));
    p.addSong(new Song(2, "B", "ArtB", "Alb", 100, 10, "U"));
    p.removeSong(0);
    cout << "Size: " << p.getSize() << " | Index 0 is now: " << p.getSong(0)->toString() << endl;
    """, "Size: 1 | Index 0 is now: B-ArtB"),

    # Test 44: Xóa bài hát ở vị trí cuối cùng (index = size - 1)
    (44, """
    Playlist p("Test 44");
    p.addSong(new Song(1, "A", "ArtA", "Alb", 100, 10, "U"));
    p.addSong(new Song(2, "B", "ArtB", "Alb", 100, 10, "U"));
    p.addSong(new Song(3, "C", "ArtC", "Alb", 100, 10, "U"));
    p.removeSong(2);
    cout << "Size: " << p.getSize() << " | Last element is now: " << p.getSong(1)->toString() << endl;
    """, "Size: 2 | Last element is now: B-ArtB"),

    # Test 45: Xóa bài hát ở vị trí giữa
    (45, """
    Playlist p("Test 45");
    p.addSong(new Song(1, "A", "ArtA", "Alb", 100, 10, "U"));
    p.addSong(new Song(2, "B", "ArtB", "Alb", 100, 10, "U"));
    p.addSong(new Song(3, "C", "ArtC", "Alb", 100, 10, "U"));
    p.removeSong(1);
    cout << "Size: " << p.getSize() << " | Index 1 is now: " << p.getSong(1)->toString() << endl;
    """, "Size: 2 | Index 1 is now: C-ArtC"),

    # Test 46: Exception - Cố gắng xóa trên Playlist rỗng
    (46, """
    Playlist p("Test 46");
    try {
        p.removeSong(0);
    } catch (const out_of_range& e) {
        cout << "Caught Exception: " << e.what() << endl;
    }
    """, "Caught Exception: Index is invalid!"),

    # Test 47: Exception - Index là số âm
    (47, """
    Playlist p("Test 47");
    p.addSong(new Song(1, "A", "ArtA", "Alb", 100, 10, "U"));
    try {
        p.removeSong(-1);
    } catch (const out_of_range& e) {
        cout << "Caught Exception: " << e.what() << endl;
    }
    """, "Caught Exception: Index is invalid!"),

    # Test 48: Exception - Index bằng hoặc lớn hơn size
    (48, """
    Playlist p("Test 48");
    p.addSong(new Song(1, "A", "ArtA", "Alb", 100, 10, "U"));
    try {
        p.removeSong(1); // Size = 1, index hợp lệ cao nhất = 0
    } catch (const out_of_range& e) {
        cout << "Caught Exception: " << e.what() << endl;
    }
    try {
        p.removeSong(5);
    } catch (const out_of_range& e) {
        cout << "Caught Exception 2: " << e.what() << endl;
    }
    """, "Caught Exception: Index is invalid!\nCaught Exception 2: Index is invalid!"),

    # Test 49: Xóa từng phần tử một cho đến khi rỗng và kiểm tra hàm empty()
    (49, """
    Playlist p("Test 49");
    p.addSong(new Song(1, "A", "ArtA", "Alb", 100, 10, "U"));
    p.addSong(new Song(2, "B", "ArtB", "Alb", 100, 10, "U"));
    p.removeSong(1); // Xóa B
    p.removeSong(0); // Xóa A
    cout << "Size: " << p.getSize() << " | Empty: " << (p.empty() ? "Yes" : "No") << endl;
    """, "Size: 0 | Empty: Yes"),

    # Test 50: Kết hợp xóa phần tử và thêm phần tử mới ngay sau đó
    (50, """
    Playlist p("Test 50");
    p.addSong(new Song(1, "A", "ArtA", "Alb", 100, 10, "U"));
    p.addSong(new Song(2, "B", "ArtB", "Alb", 100, 10, "U"));
    p.removeSong(0); // Chỉ còn B ở vị trí 0
    p.addSong(new Song(3, "C", "ArtC", "Alb", 100, 10, "U")); // C được thêm vào cuối (vị trí 1)
    cout << "Index 0: " << p.getSong(0)->toString() << " | Index 1: " << p.getSong(1)->toString() << endl;
    """, "Index 0: B-ArtB | Index 1: C-ArtC"),

    # Test 51: Xóa bài hát duy nhất trong Playlist
    (51, """
    Playlist p("Test 51");
    p.addSong(new Song(1, "Only Song", "Art", "Alb", 100, 10, "U"));
    p.removeSong(0);
    cout << "Size: " << p.getSize() << " | Empty: " << (p.empty() ? "Yes" : "No") << endl;
    """, "Size: 0 | Empty: Yes"),

    # Test 52: Xóa liên tục ở vị trí 0 (giống cách hoạt động của Queue - pop)
    (52, """
    Playlist p("Test 52");
    for(int i = 0; i < 5; i++) {
        p.addSong(new Song(i, "S" + to_string(i), "Art", "Alb", 100, 10, "U"));
    }
    p.removeSong(0); // Xóa S0
    p.removeSong(0); // Xóa S1
    cout << "Size: " << p.getSize() << " | New Head is: " << p.getSong(0)->toString() << endl;
    """, "Size: 3 | New Head is: S2-Art")
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
    print("✅ Đã tạo xong test 43 - 52 riêng cho hàm removeSong của Playlist (đã update getSize)!")

if __name__ == "__main__":
    generate()