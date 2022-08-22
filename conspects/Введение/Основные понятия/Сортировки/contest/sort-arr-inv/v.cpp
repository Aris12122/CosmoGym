#include "testlib.h"
#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)


int main(int argc, char* argv[]) {
    registerValidation(argc, argv);

    int n = inf.readInt(1, (int)1e5, "n");
    inf.readSpace();
    long long m = inf.readLong(0ll, n * 1ll * (n-1) / 2, "m");
    inf.readEoln();
    
    inf.readEof();
}
