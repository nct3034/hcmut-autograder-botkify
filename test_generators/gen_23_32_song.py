import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CPP_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "backend_core", "test_cases"))
TXT_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "backend_core", "expected_outputs"))

os.makedirs(CPP_DIR, exist_ok=True)
os.makedirs(TXT_DIR, exist_ok=True)

test_scenarios = [
    # Test 23: Khởi tạo cơ bản và gọi getter getID(), getDuration()
    (23, """
    Song s(10, "Loi Nho", "Den Vau", "Single", 245, 800, "https://...");
    cout << "ID: " << s.getID() << " | Duration: " << s.getDuration() << endl;
    """, "ID: 10 | Duration: 245"),

    # Test 24: Kiểm tra định dạng chuẩn của toString() theo đúng spec: <title>-<artist>
    (24, """
    Song s(99, "Gieo Que", "Hoang Thuy Linh", "LINK", 198, 950, "url");
    cout << "toString: " << s.toString() << endl;
    """, "toString: Gieo Que-Hoang Thuy Linh"),

    # Test 25: Edge case - Các thuộc tính chuỗi bị rỗng (Empty strings)
    (25, """
    Song s(3, "", "", "", 0, 0, "");
    cout << "ID: " << s.getID() << " | toString: " << s.toString() << endl;
    """, "ID: 3 | toString: -"),

    # Test 26: Edge case - Score rơi vào biên của đoạn [0-1000]
    (26, """
    Song* s1 = new Song(1, "Min Score", "A", "B", 10, 0, "U");
    Song* s2 = new Song(2, "Max Score", "C", "D", 500, 1000, "U");
    cout << "S1: " << s1->toString() << " | S2: " << s2->toString() << endl;
    delete s1;
    delete s2;
    """, "S1: Min Score-A | S2: Max Score-C"),

    # Test 27: Edge case - Tên bài hát và ca sĩ chứa các ký tự đặc biệt, đặc biệt là dấu gạch ngang '-'
    (27, """
    Song s(7, "A-B-C", "D-E", "F", 100, 500, "url");
    cout << s.toString() << endl;
    """, "A-B-C-D-E"),

    # Test 28: Dynamic memory allocation & Deallocation bằng mảng (ngăn ngừa memory leak)
    (28, """
    Song* arr[3];
    arr[0] = new Song(101, "S1", "A1", "Al1", 100, 100, "U1");
    arr[1] = new Song(102, "S2", "A2", "Al2", 200, 200, "U2");
    arr[2] = new Song(103, "S3", "A3", "Al3", 300, 300, "U3");
    for(int i = 0; i < 3; i++) {
        cout << arr[i]->getID() << "-" << arr[i]->getDuration() << " ";
        delete arr[i];
    }
    cout << endl;
    """, "101-100 102-200 103-300 "),

    # Test 29: Giá trị duration và ID cực lớn 
    (29, """
    Song s(999999, "Epic Long Song", "Unknown", "None", 9999999, 1000, "x");
    cout << s.getID() << " " << s.getDuration() << " " << s.toString() << endl;
    """, "999999 9999999 Epic Long Song-Unknown"),

    # Test 30: Kiểm tra tính độc lập của các đối tượng trong vùng nhớ (Memory Isolation)
    (30, """
    Song* s1 = new Song(1, "Clone", "Singer", "Alb", 150, 500, "U");
    Song* s2 = new Song(2, "Clone", "Singer", "Alb", 150, 500, "U");
    cout << (s1 != s2 ? "Different Pointers" : "Same Pointers") << " | ";
    cout << s1->toString() << " == " << s2->toString() << endl;
    delete s1;
    delete s2;
    """, "Different Pointers | Clone-Singer == Clone-Singer"),

    # Test 31: Stress test cấp phát và thu hồi vùng nhớ (Memory leak prevent check) với số lượng lớn
    (31, """
    for(int i = 0; i < 50000; i++) {
        Song* s = new Song(i, "T", "A", "Al", i, i % 1000, "U");
        if (i == 49999) {
            cout << "Passed Stress Test. Last ID: " << s->getID() << endl;
        }
        delete s;
    }
    """, "Passed Stress Test. Last ID: 49999"),

    # Test 32: Test Default Copy Constructor của Song
    (32, """
    Song s1(500, "Original", "Artist", "Album", 120, 90, "U");
    Song s2 = s1; // Copy constructor
    cout << "Copied ID: " << s2.getID() << " | " << s2.toString() << endl;
    """, "Copied ID: 500 | Original-Artist")
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
    print("✅ Đã tạo xong test 23 - 32 cho class Song!")

if __name__ == "__main__":
    generate()