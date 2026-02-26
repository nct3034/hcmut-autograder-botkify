void test_010() {
    Playlist p("Pop Hits");
    p.addSong(new Song(1, "S1", "Singer", "A", 200, 10, "U"));
    p.addSong(new Song(2, "S2", "Singer", "A", 205, 10, "U"));
    cout << "test_010 removeSong logic:" << endl;
    p.playNext(); // current is S1
    p.removeSong(0); // S1 removed -> current reset (or depends on specs, mostly -1)
    Song* nextAfterRem = p.playNext(); // Starts from 0 which is S2 now
    cout << "Next song after removal: " << nextAfterRem->toString() << endl;
}