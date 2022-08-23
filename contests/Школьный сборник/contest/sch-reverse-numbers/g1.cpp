#include "testlib.h"
#include <bits/stdc++.h>
 
using namespace std;
 
#define forn(i, n) for (int i = 0; i < int(n); i++)
#define sz(v) (int)v.size()

 
int main(int argc, char* argv[]) {
    registerGen(argc, argv, 1);

    long long k = opt<long long>(1);
    vector<long long> v(5);
    for (auto &s:v) {
        s = rnd.next(1ll, k);
    }
    
    println(v);
}
