void test_011() {
    BotkifyLinkedList<int> l;
    l.add(1);
    l.add(2);
    l.removeAt(0);
    l.removeAt(0);
    cout << "Size:" << l.size();
}
