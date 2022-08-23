#include "testlib.h"
#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)


int main(int argc, char* argv[]) {
    registerValidation(argc, argv);

    int n = inf.readInt(1, 100, "n");
    inf.readSpace();
    int m = inf.readInt(1, 100, "m");
    inf.readEoln();

    int x = inf.readInt(1, n, "x");
    inf.readSpace();
    int y = inf.readInt(1, m, "y");
    inf.readEoln();

    inf.readEof();
}
