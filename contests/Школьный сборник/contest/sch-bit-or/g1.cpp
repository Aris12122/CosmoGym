#include "testlib.h"
#include <bits/stdc++.h>
 
using namespace std;
 
#define forn(i, n) for (int i = 0; i < int(n); i++)
#define sz(v) (int)v.size()

 
int main(int argc, char* argv[]) {
    registerGen(argc, argv, 1);

    int n = opt<int>(1), q = opt<int>(2);
    long long sz = 1;
    forn(i, n) sz *= 4;

    vector<long long> a(q);
    forn(i, q) {
        a[i] = rnd.next(1ll, sz);
    }
    println(n, q);
    println(a);

}
