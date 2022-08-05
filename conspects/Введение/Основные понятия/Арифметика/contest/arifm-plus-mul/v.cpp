#include "testlib.h"
#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)


int main(int argc, char* argv[]) {
    registerValidation(argc, argv);

    inf.readInt(-100'000, 100'000, "x");
    inf.readSpace();
    inf.readInt(1, 100'000, "y");

    inf.readEoln();
    inf.readEof();
}
