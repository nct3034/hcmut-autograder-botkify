#include "main.h"
void test_004() {
    Song* s = new Song(101, "Never Gonna Give You Up", "Rick Astley", "Whenever You Need Somebody", 213, 999, "url"); cout << "test_004: " << s->getID() << " | " << s->getDuration() << " | " << s->getScore() << endl; cout << "test_004 string: " << s->toString() << endl; delete s;
}