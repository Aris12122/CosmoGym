#include "testlib.h"
#include <bits/stdc++.h>
 
using namespace std;
 
#define forn(i, n) for (int i = 0; i < int(n); i++)
#define sz(v) (int)v.size()
#define all(v) v.begin(),v.end()

 
int main(int argc, char* argv[]) {
    registerGen(argc, argv, 1);

    int n = opt<int>(1), m;
    int k = opt<int>(2);

    vector<int> a(n);
    forn(i, n) {
        a[i] = rnd.next(1, k);
    }
    vector<int> b;
    
    int yes = opt<int>(3);
    if (yes) {
        // yes;
        m = rnd.next(1, n);
        b.resize(m);
        forn(i, m) {
            b[i] = rnd.next(n);
        }
        sort(all(b));
        b.erase(unique(all(b)), b.end());
        m = sz(b);
        forn(i, m) {
            b[i] = a[b[i]];
        }
    } else {
        m = rnd.next(1, n);
        b.resize(m);

        forn(i, m) {
            b[i] = rnd.next(1, k);
        }
    }
    println(n, m);    
    println(a);
    println(b);
}
