#include "testlib.h"
#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)


int main(int argc, char* argv[]) {
    registerValidation(argc, argv);

    int n = inf.readInt(3, 10'000, "n");
    inf.readSpace();
    int m = inf.readInt(2, n, "m");
    inf.readEoln();

    vector<int> a = inf.readInts(n, 1, (int)1e9, "a");
    forn(i, n-1) {
        ensuref(a[i] < a[i+1], "a_i < a_i+1");
    }
    inf.readEoln();


    inf.readEof();
}
