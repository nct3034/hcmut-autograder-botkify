void test_011()
{
    BotkifyLinkedList<string> list;
    list.add("Hello");
    list.add("World");
    list.add("HCMUT");
    list.add("K23");

    cout << "test_011 init: " << list.toString() << endl;

    // Xóa phần tử đầu tiên ("Hello")
    list.removeAt(0);

    // Lúc này danh sách còn: World, HCMUT, K23
    // Xóa phần tử cuối cùng ("K23" - đang ở index 2)
    list.removeAt(2);

    cout << "test_011 after: " << list.toString() << endl;
}