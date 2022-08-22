#include "testlib.h"
#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)


int main(int argc, char* argv[]) {
    registerValidation(argc, argv);

    string s = inf.readLine("[a-z]{1, 255}", "s");
    string t = inf.readLine("[a-z]{1, 255}", "t");
    
    ensuref(s.size() == t.size(), "Expected string of equal length");

    inf.readEof();
}
