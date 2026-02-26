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

    (15, """
    BotkifyLinkedList<int> l;
    l.add(5);
    l.setCurrent(0);
    l.add(10);
    cout << l.getCurrent();
    """, "5"),

    (16, """
    BotkifyLinkedList<int> l;
    l.add(1);
    l.add(2);
    l.add(3);
    l.moveToEnd();
    l.moveNext();
    cout << l.getCurrent();
    """, "1"),

    (17, """
    BotkifyLinkedList<int> l;
    l.add(1);
    l.add(2);
    l.moveToStart();
    l.movePrev();
    cout << l.getCurrent();
    """, "2"),

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

    (22, """
    BotkifyLinkedList<int> l1;
    l1.add(100);
    BotkifyLinkedList<int> l2(l1);
    l1.add(200);
    cout << l2.size() << " " << l2.get(0);
    """, "1 100")
]

def generate():
    for num, code, expected in test_scenarios:
        cpp_fn = f"test_{num:03d}.cpp"
        txt_fn = f"test_{num:03d}.txt"
        with open(os.path.join(CPP_DIR, cpp_fn), "w", encoding="utf-8") as f:
            f.write('#include "main.h"\n\n')
            f.write(f"void test_{num:03d}() {{")
            f.write(code.rstrip())
            f.write("\n}\n")
        with open(os.path.join(TXT_DIR, txt_fn), "w", encoding="utf-8") as f:
            f.write(expected)
    print("✅ Đã tạo xong test 11 - 22!")

if __name__ == "__main__":
    generate()