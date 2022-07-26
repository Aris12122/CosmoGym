#include "testlib.h"
#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)


int main(int argc, char* argv[]) {
    registerValidation(argc, argv);

    inf.readDouble(-1e9, 1e9, "A");
    inf.readSpace();
    inf.readDouble(-1e9, 1e9, "B");
    inf.readEoln();
    inf.readEof();
}
