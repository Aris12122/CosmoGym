#include "testlib.h"
#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)


int main(int argc, char* argv[]) {
    registerValidation(argc, argv);

    inf.readInt(-10'000, 10'000, "x");
    inf.readSpace();
    inf.readInt(-10'000, 10'000, "y");

    inf.readEoln();
    inf.readEof();
}
