import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CPP_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "backend_core", "test_cases"))
TXT_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "backend_core", "expected_outputs"))

os.makedirs(CPP_DIR, exist_ok=True)
os.makedirs(TXT_DIR, exist_ok=True)

test_scenarios = [
    (103, """
    for(int i = 0; i < 5000; i++) {
        BotkifyLinkedList<int> list;
        for(int j = 0; j < 100; j++) {
            list.add(j);
        }
    } 
    cout << "Memory Test 103: Passed Destructor BotkifyLinkedList" << endl;
    """, "Memory Test 103: Passed Destructor BotkifyLinkedList"),

    (104, """
    BotkifyLinkedList<int> list;
    for(int i = 0; i < 100000; i++) {
        list.add(i);
    }
    for(int i = 0; i < 50000; i++) {
        list.removeAt(0); 
    }
    list.clear(); 
    cout << "Memory Test 104: Passed removeAt and clear LinkedList" << endl;
    """, "Memory Test 104: Passed removeAt and clear LinkedList"),

    (105, """
    for(int i = 0; i < 2000; i++) {
        Playlist p("Temp Playlist");
        for(int j = 0; j < 50; j++) {
            p.addSong(new Song(j, "Title", "Artist", "Album", 100, 50, "URL"));
        }
    } 
    cout << "Memory Test 105: Passed Playlist Destructor" << endl;
    """, "Memory Test 105: Passed Playlist Destructor"),

    (106, """
    Playlist p("Remover");
    for(int i = 0; i < 50000; i++) {
        p.addSong(new Song(i, "Title", "Artist", "Album", 100, 50, "URL"));
    }
    for(int i = 0; i < 50000; i++) {
        p.removeSong(0); 
    }
    cout << "Memory Test 106: Passed Playlist removeSong" << endl;
    """, "Memory Test 106: Passed Playlist removeSong"),

    (107, """
    Playlist p("Clearer");
    for(int i = 0; i < 100000; i++) {
        p.addSong(new Song(i, "Title", "Artist", "Album", 100, 50, "URL"));
    }
    p.clear(); 
    cout << "Memory Test 107: Passed Playlist clear" << endl;
    """, "Memory Test 107: Passed Playlist clear"),

    (108, """
    Playlist pA("A"), pB("B");
    for(int i = 0; i < 1000; i++) {
        pA.addSong(new Song(i, "A", "A", "A", 0, i % 10, "A"));
        pB.addSong(new Song(i, "B", "B", "B", 0, i % 10, "B"));
    }
    for(int i = 0; i < 500; i++) {
        pA.compareTo(pB, 10);
    }
    cout << "Memory Test 108: Passed compareTo memory check" << endl;
    """, "Memory Test 108: Passed compareTo memory check"),

    (109, """
    Playlist p("DP Check");
    for(int i = 0; i < 200; i++) {
        p.addSong(new Song(i, "Title", "A", "A", i % 50, 0, "A"));
    }
    for(int i = 0; i < 100; i++) {
        p.playApproximate(3); 
    }
    cout << "Memory Test 109: Passed playApproximate DP check" << endl;
    """, "Memory Test 109: Passed playApproximate DP check"),

    (110, """
    Playlist* p = new Playlist("Dynamic Playlist");
    p->addSong(new Song(1, "A", "A", "A", 10, 10, "A"));
    p->addSong(new Song(2, "B", "B", "B", 20, 20, "B"));
    delete p; 
    
    p = new Playlist("Dynamic Playlist 2");
    p->addSong(new Song(3, "C", "C", "C", 30, 30, "C"));
    delete p;
    cout << "Memory Test 110: Passed Dynamic Playlist pointer allocation" << endl;
    """, "Memory Test 110: Passed Dynamic Playlist pointer allocation"),

    (111, """
    Playlist p("Random Check");
    for(int i = 0; i < 500; i++) {
        p.addSong(new Song(i, "Title", "A", "A", i, 0, "A"));
    }
    cout.setstate(ios_base::failbit); 
    for(int i = 0; i < 100; i++) {
        p.playRandom(0);
    }
    cout.clear(); 
    cout << "Memory Test 111: Passed playRandom heavy load" << endl;
    """, "Memory Test 111: Passed playRandom heavy load"),

    (112, """
    Playlist p("Ultimate Stress");
    for(int loop = 0; loop < 50; loop++) {
        for(int i = 0; i < 1000; i++) {
            p.addSong(new Song(i, "Title", "A", "A", i, i, "A"));
        }
        for(int i = 0; i < 500; i++) {
            p.removeSong(0); 
        }
        p.getTotalScore();
        p.clear(); 
    }
    cout << "Memory Test 112: Passed THE ULTIMATE STRESS TEST!" << endl;
    """, "Memory Test 112: Passed THE ULTIMATE STRESS TEST!")
]

def generate():
    for num, code, expected in test_scenarios:
        cpp_fn = f"test_{num:03d}.cpp"
        txt_fn = f"test_{num:03d}.txt"
        with open(os.path.join(CPP_DIR, cpp_fn), "w", encoding="utf-8") as f:
            f.write(f"void test_{num:03d}() {{\n") # Đã sửa lại dòng này
            f.write(code.strip("\n")) 
            f.write("\n}\n")
        with open(os.path.join(TXT_DIR, txt_fn), "w", encoding="utf-8") as f:
            f.write(expected)
    print("✅ Đã tạo test 103 - 112 chuyên trị Memory Leak!")

if __name__ == "__main__":
    generate()