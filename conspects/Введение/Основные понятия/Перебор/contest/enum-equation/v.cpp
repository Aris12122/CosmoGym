#include "testlib.h"
#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)

const int N = (int)1e6;

int main(int argc, char* argv[]) {
    registerValidation(argc, argv);

    int A = inf.readInt(-N, N, "A");
    ensuref(A != 0, "expected A != 0");
    inf.readSpace();
    inf.readInt(-N, N, "B");
    inf.readSpace();
    inf.readInt(-N, N, "C");
    inf.readSpace();
    inf.readInt(-N, N, "D");
    inf.readEoln();
    
    inf.readEof();
}
