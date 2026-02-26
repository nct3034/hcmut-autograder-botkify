#include "main.h"

void test_003() {
    BotkifyLinkedList<string> arr;
    arr.add("apple");
    arr.add("banana");
    arr.add("cherry");
    arr.add(1, "mango");
    string removed = arr.removeAt(2);
    cout << "test_003: Removed(" << removed << ") -> " << arr.toString() << endl;
}
