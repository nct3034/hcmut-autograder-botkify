import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CPP_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "backend_core", "test_cases"))
TXT_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "backend_core", "expected_outputs"))

os.makedirs(CPP_DIR, exist_ok=True)
os.makedirs(TXT_DIR, exist_ok=True)

test_scenarios = [
    # Test 73: Khớp hoàn toàn với Example 3.4 trong Spec (A: {4,1,3,5}, B: {1,2,3}, numSong = 2)
    # Score A = 4, Score B = 2.5 => A.compareTo(B, 2) trả về true
    (73, """
    Playlist pA("ListA");
    pA.addSong(new Song(1, "A", "A", "A", 0, 4, "A"));
    pA.addSong(new Song(2, "B", "B", "B", 0, 1, "B"));
    pA.addSong(new Song(3, "C", "C", "C", 0, 3, "C"));
    pA.addSong(new Song(4, "D", "D", "D", 0, 5, "D"));
    
    Playlist pB("ListB");
    pB.addSong(new Song(5, "E", "E", "E", 0, 1, "E"));
    pB.addSong(new Song(6, "F", "F", "F", 0, 2, "F"));
    pB.addSong(new Song(7, "G", "G", "G", 0, 3, "G"));
    
    cout << "Test 73 compareTo: " << (pA.compareTo(pB, 2) ? "true" : "false") << endl;
    """, "Test 73 compareTo: true"),

    # Test 74: Phép so sánh ngược lại của Test 73 (B.compareTo(A, 2))
    # Score B (2.5) >= Score A (4) => false
    (74, """
    Playlist pA("ListA");
    pA.addSong(new Song(1, "A", "A", "A", 0, 4, "A"));
    pA.addSong(new Song(2, "B", "B", "B", 0, 1, "B"));
    pA.addSong(new Song(3, "C", "C", "C", 0, 3, "C"));
    pA.addSong(new Song(4, "D", "D", "D", 0, 5, "D"));
    
    Playlist pB("ListB");
    pB.addSong(new Song(5, "E", "E", "E", 0, 1, "E"));
    pB.addSong(new Song(6, "F", "F", "F", 0, 2, "F"));
    pB.addSong(new Song(7, "G", "G", "G", 0, 3, "G"));
    
    cout << "Test 74 compareTo: " << (pB.compareTo(pA, 2) ? "true" : "false") << endl;
    """, "Test 74 compareTo: false"),

    # Test 75: Hai Playlist có điểm trung bình bằng nhau (A >= B trả về true)
    # A = {2,2,2}, numSong=2 => Avg = 2
    # B = {1,2,1}, numSong=2 => Max(1,2)=2, Max(2,1)=2 => Avg = 2
    (75, """
    Playlist pA("A");
    pA.addSong(new Song(1, "", "", "", 0, 2, ""));
    pA.addSong(new Song(2, "", "", "", 0, 2, ""));
    pA.addSong(new Song(3, "", "", "", 0, 2, ""));
    
    Playlist pB("B");
    pB.addSong(new Song(4, "", "", "", 0, 1, ""));
    pB.addSong(new Song(5, "", "", "", 0, 2, ""));
    pB.addSong(new Song(6, "", "", "", 0, 1, ""));
    
    cout << "Test 75 compareTo: " << (pA.compareTo(pB, 2) ? "true" : "false") << endl;
    """, "Test 75 compareTo: true"),

    # Test 76: numSong = 1 (Tính trung bình cộng thông thường của toàn bộ các phần tử)
    # A = {10, 20} => Avg = 15. B = {15, 15} => Avg = 15.
    (76, """
    Playlist pA("A");
    pA.addSong(new Song(1, "", "", "", 0, 10, ""));
    pA.addSong(new Song(2, "", "", "", 0, 20, ""));
    
    Playlist pB("B");
    pB.addSong(new Song(3, "", "", "", 0, 15, ""));
    pB.addSong(new Song(4, "", "", "", 0, 15, ""));
    
    cout << "Test 76 compareTo: " << (pA.compareTo(pB, 1) ? "true" : "false") << endl;
    """, "Test 76 compareTo: true"),

    # Test 77: Kiểm tra việc sử dụng phép chia số thực (tránh lỗi chia nguyên làm sai kết quả)
    # A = {0, 1} => numSong=1 => Avg = 0.5
    # B = {0, 0, 0, 3} => numSong=1 => Avg = 0.75
    # Nếu dùng int division, Avg A = 0, Avg B = 0 => 0 >= 0 (true) => Sai.
    # Đúng chuẩn float/double: 0.5 >= 0.75 => false.
    (77, """
    Playlist pA("A");
    pA.addSong(new Song(1, "", "", "", 0, 0, ""));
    pA.addSong(new Song(2, "", "", "", 0, 1, ""));
    
    Playlist pB("B");
    pB.addSong(new Song(3, "", "", "", 0, 0, ""));
    pB.addSong(new Song(4, "", "", "", 0, 0, ""));
    pB.addSong(new Song(5, "", "", "", 0, 0, ""));
    pB.addSong(new Song(6, "", "", "", 0, 3, ""));
    
    cout << "Test 77 compareTo: " << (pA.compareTo(pB, 1) ? "true" : "false") << endl;
    """, "Test 77 compareTo: false"),

    # Test 78: numSong bằng đúng kích thước của Playlist (Tìm Max toàn dải)
    # A = {1, 5, 2} => numSong=3 => Max = 5, Avg = 5.
    # B = {4, 4, 4} => numSong=3 => Max = 4, Avg = 4.
    (78, """
    Playlist pA("A");
    pA.addSong(new Song(1, "", "", "", 0, 1, ""));
    pA.addSong(new Song(2, "", "", "", 0, 5, ""));
    pA.addSong(new Song(3, "", "", "", 0, 2, ""));
    
    Playlist pB("B");
    pB.addSong(new Song(4, "", "", "", 0, 4, ""));
    pB.addSong(new Song(5, "", "", "", 0, 4, ""));
    pB.addSong(new Song(6, "", "", "", 0, 4, ""));
    
    cout << "Test 78 compareTo: " << (pA.compareTo(pB, 3) ? "true" : "false") << endl;
    """, "Test 78 compareTo: true"),

    # Test 79: Hai dải dữ liệu đối xứng nhau, kết quả trung bình phải bằng nhau
    # A = {10, 20, 30, 40}, B = {40, 30, 20, 10}, numSong = 3
    # A Groups: Max(10,20,30)=30, Max(20,30,40)=40 => Avg = 35
    # B Groups: Max(40,30,20)=40, Max(30,20,10)=30 => Avg = 35
    # A >= B => true
    (79, """
    Playlist pA("A");
    pA.addSong(new Song(1, "", "", "", 0, 10, ""));
    pA.addSong(new Song(2, "", "", "", 0, 20, ""));
    pA.addSong(new Song(3, "", "", "", 0, 30, ""));
    pA.addSong(new Song(4, "", "", "", 0, 40, ""));
    
    Playlist pB("B");
    pB.addSong(new Song(5, "", "", "", 0, 40, ""));
    pB.addSong(new Song(6, "", "", "", 0, 30, ""));
    pB.addSong(new Song(7, "", "", "", 0, 20, ""));
    pB.addSong(new Song(8, "", "", "", 0, 10, ""));
    
    cout << "Test 79 compareTo: " << (pA.compareTo(pB, 3) ? "true" : "false") << endl;
    """, "Test 79 compareTo: true"),

    # Test 80: Toàn bộ playlist đều là 0 điểm
    (80, """
    Playlist pA("A");
    pA.addSong(new Song(1, "", "", "", 0, 0, ""));
    pA.addSong(new Song(2, "", "", "", 0, 0, ""));
    
    Playlist pB("B");
    pB.addSong(new Song(3, "", "", "", 0, 0, ""));
    pB.addSong(new Song(4, "", "", "", 0, 0, ""));
    pB.addSong(new Song(5, "", "", "", 0, 0, ""));
    
    cout << "Test 80 compareTo: " << (pA.compareTo(pB, 2) ? "true" : "false") << endl;
    """, "Test 80 compareTo: true"),

    # Test 81: Playlist A có độ dài dài hơn nhưng điểm trung bình thấp hơn hẳn
    # A = {5, 5, 5, 5, 5} => Avg = 5
    # B = {1, 9} => numSong=2 => Max(1,9)=9 => Avg = 9
    (81, """
    Playlist pA("A");
    for(int i = 0; i < 5; i++) pA.addSong(new Song(i, "", "", "", 0, 5, ""));
    
    Playlist pB("B");
    pB.addSong(new Song(6, "", "", "", 0, 1, ""));
    pB.addSong(new Song(7, "", "", "", 0, 9, ""));
    
    cout << "Test 81 compareTo: " << (pA.compareTo(pB, 2) ? "true" : "false") << endl;
    """, "Test 81 compareTo: false"),

    # Test 82: Test với các chỉ số lớn (Stress Score)
    # A = {1000, 2000}, numSong=2 => Avg = 2000
    # B = {500, 2500}, numSong=2 => Avg = 2500
    (82, """
    Playlist pA("A");
    pA.addSong(new Song(1, "", "", "", 0, 1000, ""));
    pA.addSong(new Song(2, "", "", "", 0, 2000, ""));
    
    Playlist pB("B");
    pB.addSong(new Song(3, "", "", "", 0, 500, ""));
    pB.addSong(new Song(4, "", "", "", 0, 2500, ""));
    
    cout << "Test 82 compareTo: " << (pA.compareTo(pB, 2) ? "true" : "false") << endl;
    """, "Test 82 compareTo: false")
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
    print("✅ Đã tạo xong test 73 - 82 cho hàm compareTo()!")

if __name__ == "__main__":
    generate()