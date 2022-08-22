#include "testlib.h"
#include <bits/stdc++.h>
 
using namespace std;
 
#define forn(i, n) for (int i = 0; i < int(n); i++)
#define sz(v) (int)v.size()

 
int main(int argc, char* argv[]) {
    registerGen(argc, argv, 1);

    int n = opt<int>(1);
    long long m = rnd.next(0ll, n * 1ll * (n-1) / 2);

    println(n, m);
}
