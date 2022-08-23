#include "testlib.h"
#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)


int main(int argc, char* argv[]) {
    registerValidation(argc, argv);

    int n = inf.readInt(0, 30, "n");
    inf.readSpace();
    int q = inf.readInt(1, (int)(1<<18), "q");
    inf.readEoln();

    long long sz = 1;
    for (int i = 0; i < n; i++) sz *= 4;

    inf.readLongs(q, 1, sz, "k_i");
    inf.readEoln();

    inf.readEof();
}
