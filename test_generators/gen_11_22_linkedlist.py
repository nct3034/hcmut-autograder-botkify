import os

# --- ĐOẠN FIX LỖI ĐƯỜNG DẪN TUYỆT ĐỐI ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CPP_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "backend_core", "test_cases"))
TXT_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "backend_core", "expected_outputs"))

os.makedirs(CPP_DIR, exist_ok=True)
os.makedirs(TXT_DIR, exist_ok=True)

# Danh sách kịch bản test tập trung vào Edge Cases của Linked List
# bám sát các hàm: add, removeAt, get, clear, size, moveNext, movePrev
test_scenarios = [
    (11, 
     'BotkifyLinkedList<int> l; l.add(1); l.add(2); l.removeAt(0); l.removeAt(0); cout << "Size:" << l.size();', 
     'Size:0'),
    
    (12, 
     'BotkifyLinkedList<int> l; l.add(10); l.add(20); l.add(0, 5); cout << l.toString();', 
     '5,10,20'), # Test hàm add(index, e) tại vị trí đầu (index 0)
    
    (13, 
     'BotkifyLinkedList<int> l; for(int i=0; i<50; i++) l.add(i); cout << l.size();', 
     '50'), # Test số lượng phần tử trung bình
    
    (14, 
     'BotkifyLinkedList<int> l; l.add(10); l.add(20); l.add(2, 30); cout << l.toString();', 
     '10,20,30'), # Test add(index, e) tại vị trí cuối (index == count)
    
    (15, 
     'BotkifyLinkedList<int> l; l.add(5); l.setCurrent(0); l.add(10); cout << l.getCurrent();', 
     '5'), # Test tính ổn định của currentPtr sau khi add
    
    (16, 
     'BotkifyLinkedList<int> l; l.add(1); l.add(2); l.add(3); l.moveToEnd(); l.moveNext(); cout << l.getCurrent();', 
     '1'), # Test tính chất vòng của moveNext (Tail -> Head)
    
    (17, 
     'BotkifyLinkedList<int> l; l.add(1); l.add(2); l.moveToStart(); l.movePrev(); cout << l.getCurrent();', 
     '2'), # Test tính chất vòng của movePrev (Head -> Tail)
    
    (18, 
     'BotkifyLinkedList<int> l; l.add(10); l.add(20); l.add(30); l.removeAt(1); cout << l.toString();', 
     '10,30'), # Test removeAt ở giữa
    
    (19, 
     'BotkifyLinkedList<int> l; l.add(1); l.clear(); l.add(9); cout << l.get(0) << " Size:" << l.size();', 
     '9 Size:1'), # Test clear xong rồi dùng lại
    
    (20, 
     'BotkifyLinkedList<string> l; l.add("BK"); l.add("TPHCM"); cout << l.size() << " " << l.get(1);', 
     '2 TPHCM'),
    
    (21, 
     'BotkifyLinkedList<int> l; l.add(99); l.removeAt(0); cout << (l.empty() ? "Empty" : "Not Empty");', 
     'Empty'),
    
    (22, 
     'BotkifyLinkedList<int> l1; l1.add(100); BotkifyLinkedList<int> l2(l1); l1.add(200); cout << l2.size() << " " << l2.get(0);', 
     '1 100'), # Test Copy Constructor (Deep Copy)
]

def generate():
    print(f"🛠️ Đang sửa lỗi và tạo lại Test Cases (11-22) tại: {CPP_DIR}")
    for num, code, expected in test_scenarios:
        cpp_filename = f"test_{num:03d}.cpp"
        txt_filename = f"test_{num:03d}.txt"
        
        with open(os.path.join(CPP_DIR, cpp_filename), "w", encoding="utf-8") as f:
            # Thêm main.h để nhận diện class
            f.write(f'#include "main.h"\nvoid test_{num:03d}() {{\n    {code}\n}}')
            
        with open(os.path.join(TXT_DIR, txt_filename), "w", encoding="utf-8") as f:
            f.write(expected)
            
        print(f"Updated: {cpp_filename}")
    print("✅ Đã đồng bộ bộ test 11-22 với Spec!")

if __name__ == "__main__":
    generate()