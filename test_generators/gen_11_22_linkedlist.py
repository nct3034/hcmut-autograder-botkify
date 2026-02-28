import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CPP_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "backend_core", "test_cases"))
TXT_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "backend_core", "expected_outputs"))

os.makedirs(CPP_DIR, exist_ok=True)
os.makedirs(TXT_DIR, exist_ok=True)

test_scenarios = [
    (11, """
    BotkifyLinkedList<int> l;
    l.add(1);
    l.add(2);
    l.removeAt(0);
    l.removeAt(0);
    cout << "Size:" << l.size();
    """, "Size:0"),

    (12, """
    BotkifyLinkedList<int> l;
    l.add(10);
    l.add(20);
    l.add(0, 5);
    cout << l.toString();
    """, "5,10,20"),

    (13, """
    BotkifyLinkedList<int> l;
    for(int i=0; i<50; i++) {
        l.add(i);
    }
    cout << l.size();
    """, "50"),

    (14, """
    BotkifyLinkedList<int> l;
    l.add(10);
    l.add(20);
    l.add(2, 30);
    cout << l.toString();
    """, "10,20,30"),

    # ĐÃ SỬA T015: Kiểm tra removeItem trả về true (Có trong Spec)
    (15, """
    BotkifyLinkedList<int> l;
    l.add(5);
    l.add(10);
    l.add(15);
    bool res = l.removeItem(10);
    cout << "Removed 10: " << res << " | List: " << l.toString();
    """, "Removed 10: 1 | List: 5,15"),

    # ĐÃ SỬA T016: Kiểm tra removeItem trả về false khi không tìm thấy
    (16, """
    BotkifyLinkedList<int> l;
    l.add(1);
    l.add(2);
    bool res = l.removeItem(99);
    cout << "Removed 99: " << res << " | List: " << l.toString();
    """, "Removed 99: 0 | List: 1,2"),

    # ĐÃ SỬA T017: Kiểm tra ném ngoại lệ out_of_range của hàm get()
    (17, """
    BotkifyLinkedList<int> l;
    l.add(1);
    try {
        l.get(5);
    } catch (const out_of_range& e) {
        cout << "Exception: " << e.what();
    }
    """, "Exception: Index is invalid!"),

    (18, """
    BotkifyLinkedList<int> l;
    l.add(10);
    l.add(20);
    l.add(30);
    l.removeAt(1);
    cout << l.toString();
    """, "10,30"),

    (19, """
    BotkifyLinkedList<int> l;
    l.add(1);
    l.clear();
    l.add(9);
    cout << l.get(0) << " Size:" << l.size();
    """, "9 Size:1"),

    (20, """
    BotkifyLinkedList<string> l;
    l.add("BK");
    l.add("TPHCM");
    cout << l.size() << " " << l.get(1);
    """, "2 TPHCM"),

    (21, """
    BotkifyLinkedList<int> l;
    l.add(99);
    l.removeAt(0);
    cout << (l.empty() ? "Empty" : "Not Empty");
    """, "Empty"),

    # ĐÃ SỬA T022: Thay copy constructor bằng kiểm tra ngoại lệ removeAt() rỗng
    (22, """
    BotkifyLinkedList<int> l;
    try {
        l.removeAt(0);
    } catch (const out_of_range& e) {
        cout << "Exception: " << e.what();
    }
    """, "Exception: Index is invalid!")
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
    print("✅ Đã tạo xong test 11 - 22 (Chuẩn Spec LinkedList)!")

if __name__ == "__main__":
    generate()