#include "testlib.h"
#include <bits/stdc++.h>
 
using namespace std;
 
#define forn(i, n) for (int i = 0; i < int(n); i++)
#define sz(v) (int)v.size()

 
int main(int argc, char* argv[]) {
    registerGen(argc, argv, 1);

    int n = opt<int>(1);

    string s, t;
    s = rnd.next("[a-z]{%d}", n);
    if (rnd.next(0, 1)) {
        t = s;
        shuffle(s.begin(), s.end());
    } else {
        t = rnd.next("[a-z]{%d}", n);
    }
    println(s);
    println(t);
}
