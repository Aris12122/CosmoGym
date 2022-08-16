#include "testlib.h"
#include <bits/stdc++.h>
 
using namespace std;
 
#define forn(i, n) for (int i = 0; i < int(n); i++)
#define sz(v) (int)v.size()
#define rall(v) v.rbegin(),v.rend()

 
int main(int argc, char* argv[]) {
    registerGen(argc, argv, 1);

    int n = opt<int>(1);
    int k = opt<int>(2);
    int ls = opt<int>(3);

    vector<int> a(n);
    forn(i, n) {
        a[i] = rnd.next(1, k);
    }

    if (ls) {
        sort(rall(a));
    }
    println(n);
    println(a);
    
}
