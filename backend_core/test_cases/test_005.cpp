#include "main.h"

void test_005() {
    Playlist p("Pop Hits");
    p.addSong(new Song(1, "A", "Art", "Alb", 100, 10, "url"));
    p.addSong(new Song(2, "B", "Art", "Alb", 100, 10, "url"));
    p.addSong(new Song(3, "C", "Art", "Alb", 100, 10, "url"));
    cout << "test_005 next: ";
    for(int i = 0; i < 4; i++) {
        Song* s = p.playNext();
        cout << s->toString() << (i == 3 ? "" : " -> ");
    }
    cout << endl;
    cout << "test_005 prev: ";
    for(int i = 0; i < 4; i++) {
        Song* s = p.playPrevious();
        cout << s->toString() << (i == 3 ? "" : " -> ");
    }
    cout << endl;
}
