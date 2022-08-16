#include "testlib.h"
#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)


int main(int argc, char* argv[]) {
    registerValidation(argc, argv);

    int n = inf.readInt(1, 100'000, "n");
    inf.readSpace();
    int m = inf.readInt(1, 100'000, "m");
    inf.readEoln();

    inf.readInts(n, 1, (int)1e9, "a");
    inf.readEoln();

    forn(i, m) {
        int l = inf.readInt(1, (int)1e9, "l");
        inf.readSpace();
        inf.readInt(l, (int)1e9, "r");
        inf.readEoln();
    }

    inf.readEof();
}
