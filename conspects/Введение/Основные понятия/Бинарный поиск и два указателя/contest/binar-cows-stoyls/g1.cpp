#include "testlib.h"
#include <bits/stdc++.h>
 
using namespace std;
 
#define forn(i, n) for (int i = 0; i < int(n); i++)
#define sz(v) (int)v.size()
#define all(v) v.begin(),v.end()

 
int main(int argc, char* argv[]) {
    registerGen(argc, argv, 1);

    int n = opt<int>(1);
    int N = opt<int>(2);
    

    vector<int> a(n);
    forn(i, n) {
        a[i] = rnd.next(1, N);
    }
    sort(all(a));
    a.erase(unique(all(a)), a.end());
    n = sz(a);

    int m = rnd.next(2, n - 1);

    println(n, m);
    println(a);
}
