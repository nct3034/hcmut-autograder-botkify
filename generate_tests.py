import os

# Định nghĩa đường dẫn
TEST_CASES_DIR = os.path.join("backend_core", "test_cases")
EXPECTED_DIR = os.path.join("backend_core", "expected_outputs")

# Đảm bảo thư mục đã tồn tại
os.makedirs(TEST_CASES_DIR, exist_ok=True)
os.makedirs(EXPECTED_DIR, exist_ok=True)

# Kho dữ liệu Test Case
data = {
    "test_001": {
        "cpp": """void test_001() {
    BotkifyLinkedList<int> arr;
    arr.add(10);
    arr.add(20);
    arr.add(30);
    cout << "test_001: " << arr.toString() << endl;
}""",
        "txt": "test_001: 10,20,30"
    },
    "test_002": {
        "cpp": """void test_002() {
    BotkifyLinkedList<int> arr;
    arr.add(5);
    arr.add(15);
    arr.add(25);
    cout << "test_002: " << arr.toString() << endl;
}""",
        "txt": "test_002: 5,15,25"
    },
    "test_003": {
        "cpp": """void test_003() {
    BotkifyLinkedList<string> arr;
    arr.add("apple");
    arr.add("banana");
    arr.add("cherry");

    arr.add(1, "mango");
    string removed = arr.removeAt(2);

    cout << "test_003: Removed(" << removed << ") -> " << arr.toString() << endl;
}""",
        "txt": "test_003: Removed(banana) -> apple,mango,cherry"
    },
    "test_004": {
        "cpp": """void test_004() {
    Song* s = new Song(101, "Never Gonna Give You Up", "Rick Astley", "Whenever You Need Somebody", 213, 999, "url");

    cout << "test_004: " << s->getID() << " | " << s->getDuration() << " | " << s->getScore() << endl;
    cout << "test_004 string: " << s->toString() << endl;

    delete s;
}""",
        "txt": "test_004: 101 | 213 | 999\ntest_004 string: Never Gonna Give You Up-Rick Astley"
    },
    "test_005": {
        "cpp": """void test_005() {
    Playlist p("Pop Hits");
    p.addSong(new Song(1, "A", "Art", "Alb", 100, 10, "url"));
    p.addSong(new Song(2, "B", "Art", "Alb", 100, 10, "url"));
    p.addSong(new Song(3, "C", "Art", "Alb", 100, 10, "url"));

    cout << "test_005 next: ";
    for(int i = 0; i < 4; i++) {
        Song* s = p.playNext();
        cout << s->toString() << (i == 3 ? "" : " -> ");
    }
    cout << endl;

    cout << "test_005 prev: ";
    for(int i = 0; i < 4; i++) {
        Song* s = p.playPrevious();
        cout << s->toString() << (i == 3 ? "" : " -> ");
    }
    cout << endl;
}""",
        "txt": "test_005 next: B-Art -> C-Art -> A-Art -> B-Art\ntest_005 prev: A-Art -> C-Art -> B-Art -> A-Art"
    },
    "test_006": {
        "cpp": """void test_006() {
    Playlist p("ListA");
    p.addSong(new Song(1, "A", "A", "A", 0, 4, "A"));
    p.addSong(new Song(2, "B", "B", "B", 0, 1, "B"));
    p.addSong(new Song(3, "C", "C", "C", 0, 3, "C"));
    p.addSong(new Song(4, "D", "D", "D", 0, 5, "D"));

    cout << "test_006 getTotalScore (Spec 3.3): " << p.getTotalScore() << endl;
}""",
        "txt": "test_006 getTotalScore (Spec 3.3): 114"
    },
    "test_007": {
        "cpp": """void test_007() {
    Playlist pA("ListA");
    pA.addSong(new Song(1, "A", "A", "A", 0, 4, "A"));
    pA.addSong(new Song(2, "B", "B", "B", 0, 1, "B"));
    pA.addSong(new Song(3, "C", "C", "C", 0, 3, "C"));
    pA.addSong(new Song(4, "D", "D", "D", 0, 5, "D"));

    Playlist pB("ListB");
    pB.addSong(new Song(5, "E", "E", "E", 0, 1, "E"));
    pB.addSong(new Song(6, "F", "F", "F", 0, 2, "F"));
    pB.addSong(new Song(7, "G", "G", "G", 0, 3, "G"));

    cout << "test_007 compareTo (Spec 3.4): " << (pA.compareTo(pB, 2) ? "true" : "false") << endl;
}""",
        "txt": "test_007 compareTo (Spec 3.4): true"
    },
    "test_008": {
        "cpp": """void test_008() {
    Playlist p("List");
    p.addSong(new Song(1, "A", "A", "A", 50, 0, "A"));
    p.addSong(new Song(2, "B", "B", "B", 60, 0, "B"));
    p.addSong(new Song(3, "C", "C", "C", 30, 0, "C"));
    p.addSong(new Song(4, "D", "D", "D", 90, 0, "D"));
    p.addSong(new Song(5, "E", "E", "E", 100, 0, "E"));

    cout << "test_008 playApproximate (Spec 3.5): " << p.playApproximate(1) << endl;
}""",
        "txt": "test_008 playApproximate (Spec 3.5): 50"
    },
    "test_009": {
        "cpp": """void test_009() {
    Playlist p("TestPlay");
    p.addSong(new Song(1, "A", "Art", "Alb", 50, 4, "url"));
    p.addSong(new Song(2, "B", "Art", "Alb", 60, 1, "url"));
    p.addSong(new Song(3, "C", "Art", "Alb", 30, 3, "url"));
    p.addSong(new Song(4, "D", "Art", "Alb", 90, 5, "url"));
    p.addSong(new Song(5, "E", "Art", "Alb", 100, 5, "url"));

    cout << "test_009 playRandom(0): ";
    p.playRandom(0);
}""",
        "txt": "test_009 playRandom(0): A-Art,B-Art,D-Art,E-Art"
    },
    "test_010": {
        "cpp": """void test_010() {
    Playlist p("Pop Hits");
    p.addSong(new Song(1, "S1", "Singer", "A", 200, 10, "U"));
    p.addSong(new Song(2, "S2", "Singer", "A", 205, 10, "U"));
    cout << "test_010 removeSong logic:" << endl;
    p.playNext(); // current is S1
    p.removeSong(0); // S1 removed -> current reset (or depends on specs, mostly -1)
    Song* nextAfterRem = p.playNext(); // Starts from 0 which is S2 now
    cout << "Next song after removal: " << nextAfterRem->toString() << endl;
}""",
        "txt": "test_010 removeSong logic:\nNext song after removal: S2-Singer"
    }
}

print("Bắt đầu sinh file tự động...")

# Vòng lặp đẻ file
for test_id, content in data.items():
    # Ghi file .cpp
    cpp_path = os.path.join(TEST_CASES_DIR, f"{test_id}.cpp")
    with open(cpp_path, "w", encoding="utf-8") as f:
        f.write(content["cpp"])
    
    # Ghi file .txt
    txt_path = os.path.join(EXPECTED_DIR, f"{test_id}.txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(content["txt"])
    
    print(f"✅ Đã tạo thành công {test_id}.cpp và {test_id}.txt")

print("Hoàn tất! Giờ bạn có thể mở web lên chấm bài rồi!")