#include "testlib.h"
#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)


int main(int argc, char* argv[]) {
    registerValidation(argc, argv);

    int n = inf.readInt(1, 100, "N");
    ensuref(n % 2 == 0, "expected even N");
    inf.readEoln();

    inf.readInts(n, 1, (int)1e6, "a");
    inf.readEoln();

    inf.readEof();
}
