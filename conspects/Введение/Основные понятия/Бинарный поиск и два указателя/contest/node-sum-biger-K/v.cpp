#include "testlib.h"
#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)


int main(int argc, char* argv[]) {
    registerValidation(argc, argv);

    int n = inf.readInt(1, 200'000, "n");
    inf.readSpace();
    inf.readLong(1LL, 1'000'000'000'000LL, "S");
    inf.readEoln();

    inf.readInts(n, 1, (int)1e9, "a");
    inf.readEoln();

    inf.readEof();
}
