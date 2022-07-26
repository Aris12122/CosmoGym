#include "testlib.h"
#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)


int main(int argc, char* argv[]) {
    registerValidation(argc, argv);

    int t = inf.readInt(1, 10'000, "t");
    inf.readEoln();

    int sum = 0;
    forn(tt, t) {
        setTestCase(tt + 1);
        inf.readEoln();
        int n = inf.readInt(1, 1000, "n");
        inf.readSpace();
        int m = inf.readInt(1, 1000, "m");
        inf.readEoln();

        sum += n * m;
        ensuref(sum <= 1'000'000, "sum <= 1'000'000");

        pattern p("[0-9]{" + to_string(m) + "}");
        forn(i, n+1)
            inf.readLine(p, "phone number");
    }

    inf.readEof();
}
