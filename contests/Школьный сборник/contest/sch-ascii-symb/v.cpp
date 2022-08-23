#include "testlib.h"
#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)


int main(int argc, char* argv[]) {
    registerValidation(argc, argv);

    int c = (int)inf.readChar();
    ensuref(33 <= c && c <= 127, "Expected char with code [33, 127]");
    inf.readEoln();
    inf.readEof();
}
