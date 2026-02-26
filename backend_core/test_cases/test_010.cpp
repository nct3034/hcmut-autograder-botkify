#include "main.h"
void test_010() {
    Playlist p("Pop Hits"); p.addSong(new Song(1, "S1", "Singer", "A", 200, 10, "U")); p.addSong(new Song(2, "S2", "Singer", "A", 205, 10, "U")); cout << "test_010 removeSong logic:" << endl; p.playNext(); p.removeSong(0); Song* nextAfterRem = p.playNext(); cout << "Next song after removal: " << nextAfterRem->toString() << endl;
}