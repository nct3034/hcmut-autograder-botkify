#include "main.h"

void test_006() {
    Playlist p("ListA");
    p.addSong(new Song(1, "A", "A", "A", 0, 4, "A"));
    p.addSong(new Song(2, "B", "B", "B", 0, 1, "B"));
    p.addSong(new Song(3, "C", "C", "C", 0, 3, "C"));
    p.addSong(new Song(4, "D", "D", "D", 0, 5, "D"));
    cout << "test_006 getTotalScore (Spec 3.3): " << p.getTotalScore() << endl;
}
