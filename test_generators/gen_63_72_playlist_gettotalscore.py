import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CPP_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "backend_core", "test_cases"))
TXT_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "backend_core", "expected_outputs"))

os.makedirs(CPP_DIR, exist_ok=True)
os.makedirs(TXT_DIR, exist_ok=True)

test_scenarios = [
    # Test 63: Khớp hoàn toàn với Example 3.3 trong Spec (Score: {4, 1, 3, 5} -> Total: 114)
    (63, """
    Playlist p("Spec Example");
    p.addSong(new Song(1, "A", "A", "A", 0, 4, "U"));
    p.addSong(new Song(2, "B", "B", "B", 0, 1, "U"));
    p.addSong(new Song(3, "C", "C", "C", 0, 3, "U"));
    p.addSong(new Song(4, "D", "D", "D", 0, 5, "U"));
    cout << "Test 63 Score: " << p.getTotalScore() << endl;
    """, "Test 63 Score: 114"),

    # Test 64: Playlist chỉ có đúng 1 bài hát (Score: {10} -> 10*10 = 100)
    (64, """
    Playlist p("Single Song");
    p.addSong(new Song(1, "A", "A", "A", 0, 10, "U"));
    cout << "Test 64 Score: " << p.getTotalScore() << endl;
    """, "Test 64 Score: 100"),

    # Test 65: Các bài hát có điểm số bằng nhau (Score: {2, 2, 2})
    # L1: 4 + 4 + 4 = 12
    # L2: 2*(4) + 2*(4) = 16
    # L3: 2*(6) = 12
    # Total = 40
    (65, """
    Playlist p("Equal Scores");
    p.addSong(new Song(1, "A", "A", "A", 0, 2, "U"));
    p.addSong(new Song(2, "B", "B", "B", 0, 2, "U"));
    p.addSong(new Song(3, "C", "C", "C", 0, 2, "U"));
    cout << "Test 65 Score: " << p.getTotalScore() << endl;
    """, "Test 65 Score: 40"),

    # Test 66: Chuỗi điểm giảm dần (Score: {5, 3, 1})
    # L1: 25 + 9 + 1 = 35
    # L2: 3*(8) + 1*(4) = 28
    # L3: 1*(9) = 9
    # Total = 72
    (66, """
    Playlist p("Decreasing");
    p.addSong(new Song(1, "A", "A", "A", 0, 5, "U"));
    p.addSong(new Song(2, "B", "B", "B", 0, 3, "U"));
    p.addSong(new Song(3, "C", "C", "C", 0, 1, "U"));
    cout << "Test 66 Score: " << p.getTotalScore() << endl;
    """, "Test 66 Score: 72"),

    # Test 67: Chuỗi điểm tăng dần (Score: {1, 3, 5} -> Total = 72)
    (67, """
    Playlist p("Increasing");
    p.addSong(new Song(1, "A", "A", "A", 0, 1, "U"));
    p.addSong(new Song(2, "B", "B", "B", 0, 3, "U"));
    p.addSong(new Song(3, "C", "C", "C", 0, 5, "U"));
    cout << "Test 67 Score: " << p.getTotalScore() << endl;
    """, "Test 67 Score: 72"),

    # Test 68: Có bài hát điểm 0 ở giữa, làm đứt đoạn tích điểm (Score: {4, 0, 4})
    # L1: 16 + 0 + 16 = 32
    # L2: 0 + 0 = 0
    # L3: 0
    # Total = 32
    (68, """
    Playlist p("Zero in Middle");
    p.addSong(new Song(1, "A", "A", "A", 0, 4, "U"));
    p.addSong(new Song(2, "B", "B", "B", 0, 0, "U"));
    p.addSong(new Song(3, "C", "C", "C", 0, 4, "U"));
    cout << "Test 68 Score: " << p.getTotalScore() << endl;
    """, "Test 68 Score: 32"),

    # Test 69: Edge case - Chỉ có 2 phần tử (Score: {10, 20})
    # L1: 100 + 400 = 500
    # L2: 10*(30) = 300
    # Total = 800
    (69, """
    Playlist p("Two Elements");
    p.addSong(new Song(1, "A", "A", "A", 0, 10, "U"));
    p.addSong(new Song(2, "B", "B", "B", 0, 20, "U"));
    cout << "Test 69 Score: " << p.getTotalScore() << endl;
    """, "Test 69 Score: 800"),

    # Test 70: Tất cả bài hát đều 0 điểm (Score: {0, 0, 0})
    (70, """
    Playlist p("All Zeroes");
    p.addSong(new Song(1, "A", "A", "A", 0, 0, "U"));
    p.addSong(new Song(2, "B", "B", "B", 0, 0, "U"));
    p.addSong(new Song(3, "C", "C", "C", 0, 0, "U"));
    cout << "Test 70 Score: " << p.getTotalScore() << endl;
    """, "Test 70 Score: 0"),

    # Test 71: Test điểm với con số lớn (Score: {100, 200, 300})
    # L1: 10000 + 40000 + 90000 = 140000
    # L2: 100*300 + 200*500 = 130000
    # L3: 100*600 = 60000
    # Total = 330000
    (71, """
    Playlist p("Large Values");
    p.addSong(new Song(1, "A", "A", "A", 0, 100, "U"));
    p.addSong(new Song(2, "B", "B", "B", 0, 200, "U"));
    p.addSong(new Song(3, "C", "C", "C", 0, 300, "U"));
    cout << "Test 71 Score: " << p.getTotalScore() << endl;
    """, "Test 71 Score: 330000"),

    # Test 72: Edge case cực đoan - Playlist rỗng (trả về 0)
    (72, """
    Playlist p("Empty Playlist");
    cout << "Test 72 Score: " << p.getTotalScore() << endl;
    """, "Test 72 Score: 0")
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
    print("✅ Đã tạo xong test 63 - 72 cho hàm getTotalScore()!")

if __name__ == "__main__":
    generate()