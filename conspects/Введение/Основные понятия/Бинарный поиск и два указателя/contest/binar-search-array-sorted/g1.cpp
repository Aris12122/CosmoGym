#include "testlib.h"
#include <bits/stdc++.h>
 
using namespace std;
 
#define forn(i, n) for (int i = 0; i < int(n); i++)
#define sz(v) (int)v.size()

 
int main(int argc, char* argv[]) {
    registerGen(argc, argv, 1);

    int n = opt<int>(1), m = opt<int>(2);
    int k = opt<int>(3);
    if (k == 100) k = 100;
    else k = (int)1e9;

    vector<int> a(n);
    forn(i, n) {
        a[i] = rnd.next(1, k);

    }
    println(n, m);
    println(a);

    forn(i, m) {
        println(rnd.next(1, k));
    }
}
