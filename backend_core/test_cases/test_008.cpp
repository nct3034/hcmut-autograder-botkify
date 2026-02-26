void test_008() {
    Playlist p("List");
    p.addSong(new Song(1, "A", "A", "A", 50, 0, "A"));
    p.addSong(new Song(2, "B", "B", "B", 60, 0, "B"));
    p.addSong(new Song(3, "C", "C", "C", 30, 0, "C"));
    p.addSong(new Song(4, "D", "D", "D", 90, 0, "D"));
    p.addSong(new Song(5, "E", "E", "E", 100, 0, "E"));

    cout << "test_008 playApproximate (Spec 3.5): " << p.playApproximate(1) << endl;
}