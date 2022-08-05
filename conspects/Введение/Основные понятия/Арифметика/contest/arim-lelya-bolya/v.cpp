#include "testlib.h"
#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)


int main(int argc, char* argv[]) {
    registerValidation(argc, argv);

    int a = inf.readInt(1, 1'000'000, "a");
    inf.readSpace();
    int b = inf.readInt(1, 1'000'000, "b");

    inf.ensuref(a != b, "expected a != b");
    inf.readEoln();
    inf.readEof();
}
