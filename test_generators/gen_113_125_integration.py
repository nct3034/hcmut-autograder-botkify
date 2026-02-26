import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CPP_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "backend_core", "test_cases"))
TXT_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "backend_core", "expected_outputs"))

os.makedirs(CPP_DIR, exist_ok=True)
os.makedirs(TXT_DIR, exist_ok=True)

test_scenarios = [
    # Test 113: Basic Integration - Add, Size, Empty, Score, PlayNext
    (113, """
    Playlist p("T113");
    p.addSong(new Song(1, "A", "A", "A", 10, 5, "U"));
    p.addSong(new Song(2, "B", "B", "B", 20, 10, "U"));
    cout << p.size() << " " << p.empty() << " " << p.getTotalScore() << endl;
    cout << p.playNext()->toString() << endl;
    """, "2 0 200\nB-B"),

    # Test 114: Multiple removes altering the playlist structure, then checking bounds
    (114, """
    Playlist p("T114");
    for(int i=0; i<5; i++) p.addSong(new Song(i, to_string(i), "A", "A", i*10, i, "U"));
    p.removeSong(4); 
    p.removeSong(2); 
    p.removeSong(0);
    cout << p.size() << " " << p.getSong(0)->toString() << " " << p.getSong(1)->toString() << endl;
    """, "2 1-A 3-A"),

    # Test 115: Use BotkifyLinkedList side-by-side with Playlist
    (115, """
    BotkifyLinkedList<string> lst;
    lst.add("S1"); lst.add("S2"); lst.add("S3");
    lst.removeAt(1); // Keeps S1, S3
    Playlist p("T115");
    p.addSong(new Song(1, lst.get(0), "Art", "Alb", 10, 10, "U"));
    p.addSong(new Song(2, lst.get(1), "Art", "Alb", 20, 20, "U"));
    cout << p.playNext()->toString() << " " << p.getTotalScore() << endl;
    """, "S3-Art 800"),

    # Test 116: Cross-comparing CompareTo on 2 different Playlists
    (116, """
    Playlist p1("P1"); p1.addSong(new Song(1,"A","A","A",0,10,"U"));
    Playlist p2("P2"); p2.addSong(new Song(2,"B","B","B",0,20,"U"));
    cout << p1.compareTo(p2, 1) << " " << p2.compareTo(p1, 1) << endl;
    """, "0 1"),

    # Test 117: PlayApproximate combined with PlayNext pointer consistency
    (117, """
    Playlist p("T117");
    p.addSong(new Song(1,"A","A","A",30,0,"U"));
    p.addSong(new Song(2,"B","B","B",10,0,"U"));
    p.addSong(new Song(3,"C","C","C",50,0,"U"));
    cout << p.playApproximate(1) << endl;
    cout << p.playNext()->toString() << endl;
    """, "20\nB-B"),

    # Test 118: Catching exceptions accurately after clearing the playlist
    (118, """
    Playlist p("T118");
    p.addSong(new Song(1,"A","A","A",0,0,"U"));
    p.clear();
    cout << p.empty() << " ";
    try { p.playPrevious(); } catch(exception& e) { cout << e.what() << endl; }
    """, "1 Index is invalid!"),

    # Test 119: Dynamic getTotalScore updating correctly as songs are added
    (119, """
    Playlist p("T119");
    cout << p.getTotalScore() << " ";
    p.addSong(new Song(1,"A","A","A",0,2,"U"));
    cout << p.getTotalScore() << " ";
    p.addSong(new Song(2,"B","B","B",0,3,"U"));
    cout << p.getTotalScore() << endl;
    """, "0 4 23"),

    # Test 120: Wrap around PlayNext and PlayPrev repeatedly
    (120, """
    Playlist p("T120");
    p.addSong(new Song(1,"A","A","A",0,0,"U"));
    p.addSong(new Song(2,"B","B","B",0,0,"U"));
    for(int i=0; i<3; i++) p.playNext(); // B -> A -> B
    cout << p.playPrevious()->toString() << endl; // Prev of B is A
    """, "A-A"),

    # Test 121: PlayRandom avoiding ties effectively
    (121, """
    Playlist p("T121");
    p.addSong(new Song(1,"A","A","A",10,10,"U"));
    p.addSong(new Song(2,"B","B","B",50,20,"U"));
    p.addSong(new Song(3,"C","C","C",100,30,"U"));
    cout << "R: "; p.playRandom(1); cout << endl; // From B(50), A is not >50, so jumps to C(100)
    """, "R: B-B,C-C\n"),

    # Test 122: PlayApproximate with differing steps on the same list
    (122, """
    Playlist p("T122");
    p.addSong(new Song(1,"A","A","A",10,0,"U"));
    p.addSong(new Song(2,"B","B","B",100,0,"U"));
    p.addSong(new Song(3,"C","C","C",20,0,"U"));
    p.addSong(new Song(4,"D","D","D",100,0,"U"));
    p.addSong(new Song(5,"E","E","E",30,0,"U"));
    cout << p.playApproximate(0) << " " << p.playApproximate(1) << endl;
    """, "320 20"),

    # Test 123: PlayRandom terminating properly
    (123, """
    Playlist p("T123");
    p.addSong(new Song(1,"A","A","A",10,0,"U"));
    p.addSong(new Song(2,"B","B","B",50,0,"U"));
    p.addSong(new Song(3,"C","C","C",20,0,"U"));
    p.addSong(new Song(4,"D","D","D",40,0,"U"));
    cout << "R: "; p.playRandom(0); cout << endl;
    """, "R: A-A,B-B\n"),

    # Test 124: Comprehensive Error Handling Accumulator
    (124, """
    Playlist p("T124");
    int errors = 0;
    try { p.getSong(-1); } catch(...) { errors++; }
    try { p.removeSong(0); } catch(...) { errors++; }
    try { p.playNext(); } catch(...) { errors++; }
    cout << "Errors caught: " << errors << endl;
    """, "Errors caught: 3"),

    # Test 125: THE GRAND FINALE - Mixing everything
    (125, """
    Playlist p("T125");
    p.addSong(new Song(1,"A","A","A",10,2,"U"));
    p.addSong(new Song(2,"B","B","B",30,4,"U"));
    p.addSong(new Song(3,"C","C","C",20,6,"U"));
    cout << p.size() << " " << p.getTotalScore() << " " << p.playApproximate(1) << " ";
    p.removeSong(1);
    cout << p.size() << " " << p.playNext()->toString() << endl;
    """, "3 132 10 2 C-C")
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
    print("✅ Đã tạo xong 13 test integration tổng hợp (113 - 125)!")

if __name__ == "__main__":
    generate()