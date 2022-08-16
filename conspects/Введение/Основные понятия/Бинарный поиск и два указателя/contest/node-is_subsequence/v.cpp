#include "testlib.h"
#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)


int main(int argc, char* argv[]) {
    registerValidation(argc, argv);

    int n = inf.readInt(1, 200'000, "n");
    inf.readSpace();
    int m = inf.readInt(1, n, "m");
    inf.readEoln();

    inf.readInts(n, 1, (int)1e9, "a");
    inf.readEoln();
    inf.readInts(m, 1, (int)1e9, "b");
    inf.readEoln();

    inf.readEof();
}
