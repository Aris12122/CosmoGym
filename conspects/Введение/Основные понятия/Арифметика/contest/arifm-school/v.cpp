#include "testlib.h"
#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)


int main(int argc, char* argv[]) {
    registerValidation(argc, argv);

    int a = inf.readInt(1, 1000, "A");
    inf.readSpace();
    inf.readInt(a + 1, 1000, "B");
    inf.readSpace();
    
    inf.readInt(1, 1000, "X");
    inf.readSpace();
    inf.readInt(1, 1000, "Y");
    
    inf.readEoln();
    inf.readEof();
}
