import os

# --- FIX LỖI ĐƯỜNG DẪN TUYỆT ĐỐI ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CPP_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "backend_core", "test_cases"))
TXT_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "backend_core", "expected_outputs"))

os.makedirs(CPP_DIR, exist_ok=True)
os.makedirs(TXT_DIR, exist_ok=True)

# Danh sách test case bám sát nội dung bạn cung cấp
basic_tests = [
    (1, 
     'BotkifyLinkedList<int> arr; arr.add(10); arr.add(20); arr.add(30); cout << "test_001: " << arr.toString() << endl;', 
     'test_001: 10,20,30'),
    
    (2, 
     'BotkifyLinkedList<int> arr; arr.add(5); arr.add(15); arr.add(25); cout << "test_002: " << arr.toString() << endl;', 
     'test_002: 5,15,25'),
    
    (3, 
     'BotkifyLinkedList<string> arr; arr.add("apple"); arr.add("banana"); arr.add("cherry"); arr.add(1, "mango"); string removed = arr.removeAt(2); cout << "test_003: Removed(" << removed << ") -> " << arr.toString() << endl;', 
     'test_003: Removed(banana) -> apple,mango,cherry'),
    
    (4, 
     'Song* s = new Song(101, "Never Gonna Give You Up", "Rick Astley", "Whenever You Need Somebody", 213, 999, "url"); cout << "test_004: " << s->getID() << " | " << s->getDuration() << " | " << s->getScore() << endl; cout << "test_004 string: " << s->toString() << endl; delete s;', 
     'test_004: 101 | 213 | 999\ntest_004 string: Never Gonna Give You Up-Rick Astley'),
    
    (5, 
     'Playlist p("Pop Hits"); p.addSong(new Song(1, "A", "Art", "Alb", 100, 10, "url")); p.addSong(new Song(2, "B", "Art", "Alb", 100, 10, "url")); p.addSong(new Song(3, "C", "Art", "Alb", 100, 10, "url")); cout << "test_005 next: "; for(int i = 0; i < 4; i++) { Song* s = p.playNext(); cout << s->toString() << (i == 3 ? "" : " -> "); } cout << endl; cout << "test_005 prev: "; for(int i = 0; i < 4; i++) { Song* s = p.playPrevious(); cout << s->toString() << (i == 3 ? "" : " -> "); } cout << endl;', 
     'test_005 next: B-Art -> C-Art -> A-Art -> B-Art\ntest_005 prev: A-Art -> C-Art -> B-Art -> A-Art'),
    
    (6, 
     'Playlist p("ListA"); p.addSong(new Song(1, "A", "A", "A", 0, 4, "A")); p.addSong(new Song(2, "B", "B", "B", 0, 1, "B")); p.addSong(new Song(3, "C", "C", "C", 0, 3, "C")); p.addSong(new Song(4, "D", "D", "D", 0, 5, "D")); cout << "test_006 getTotalScore (Spec 3.3): " << p.getTotalScore() << endl;', 
     'test_006 getTotalScore (Spec 3.3): 114'),
    
    (7, 
     'Playlist pA("ListA"); pA.addSong(new Song(1, "A", "A", "A", 0, 4, "A")); pA.addSong(new Song(2, "B", "B", "B", 0, 1, "B")); pA.addSong(new Song(3, "C", "C", "C", 0, 3, "C")); pA.addSong(new Song(4, "D", "D", "D", 0, 5, "D")); Playlist pB("ListB"); pB.addSong(new Song(5, "E", "E", "E", 0, 1, "E")); pB.addSong(new Song(6, "F", "F", "F", 0, 2, "F")); pB.addSong(new Song(7, "G", "G", "G", 0, 3, "G")); cout << "test_007 compareTo (Spec 3.4): " << (pA.compareTo(pB, 2) ? "true" : "false") << endl;', 
     'test_007 compareTo (Spec 3.4): true'),
    
    (8, 
     'Playlist p("List"); p.addSong(new Song(1, "A", "A", "A", 50, 0, "A")); p.addSong(new Song(2, "B", "B", "B", 60, 0, "B")); p.addSong(new Song(3, "C", "C", "C", 30, 0, "C")); p.addSong(new Song(4, "D", "D", "D", 90, 0, "D")); p.addSong(new Song(5, "E", "E", "E", 100, 0, "E")); cout << "test_008 playApproximate (Spec 3.5): " << p.playApproximate(1) << endl;', 
     'test_008 playApproximate (Spec 3.5): 50'),
    
    (9, 
     'Playlist p("TestPlay"); p.addSong(new Song(1, "A", "Art", "Alb", 50, 4, "url")); p.addSong(new Song(2, "B", "Art", "Alb", 60, 1, "url")); p.addSong(new Song(3, "C", "Art", "Alb", 30, 3, "url")); p.addSong(new Song(4, "D", "Art", "Alb", 90, 5, "url")); p.addSong(new Song(5, "E", "Art", "Alb", 100, 5, "url")); cout << "test_009 playRandom(0): "; p.playRandom(0);', 
     'test_009 playRandom(0): A-Art,B-Art,D-Art,E-Art'),
    
    (10, 
     'Playlist p("Pop Hits"); p.addSong(new Song(1, "S1", "Singer", "A", 200, 10, "U")); p.addSong(new Song(2, "S2", "Singer", "A", 205, 10, "U")); cout << "test_010 removeSong logic:" << endl; p.playNext(); p.removeSong(0); Song* nextAfterRem = p.playNext(); cout << "Next song after removal: " << nextAfterRem->toString() << endl;', 
     'test_010 removeSong logic:\nNext song after removal: S2-Singer'),
]

def generate():
    print(f"🚀 Đang khởi tạo 10 test cases mẫu tại: {CPP_DIR}")
    for num, code, expected in basic_tests:
        cpp_fn = f"test_{num:03d}.cpp"
        txt_fn = f"test_{num:03d}.txt"
        
        with open(os.path.join(CPP_DIR, cpp_fn), "w", encoding="utf-8") as f:
            f.write(f"#include \"main.h\"\nvoid test_{num:03d}() {{\n    {code}\n}}")
            
        with open(os.path.join(TXT_DIR, txt_fn), "w", encoding="utf-8") as f:
            f.write(expected)
            
    print("✅ Hoàn thành cập nhật 10 Test Cases đầu tiên!")

if __name__ == "__main__":
    generate()