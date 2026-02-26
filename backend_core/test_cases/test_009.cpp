void test_009() {
    Playlist p("TestPlay");
    p.addSong(new Song(1, "A", "Art", "Alb", 50, 4, "url"));
    p.addSong(new Song(2, "B", "Art", "Alb", 60, 1, "url"));
    p.addSong(new Song(3, "C", "Art", "Alb", 30, 3, "url"));
    p.addSong(new Song(4, "D", "Art", "Alb", 90, 5, "url"));
    p.addSong(new Song(5, "E", "Art", "Alb", 100, 5, "url"));

    cout << "test_009 playRandom(0): ";
    p.playRandom(0);
}