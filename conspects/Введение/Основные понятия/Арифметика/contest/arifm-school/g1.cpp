#include "testlib.h"
#include <bits/stdc++.h>
 
using namespace std;
 
#define forn(i, n) for (int i = 0; i < int(n); i++)
#define sz(v) (int)v.size()

 
int main(int argc, char* argv[]) {
    registerGen(argc, argv, 1);

    vector<int> v(4);

    if (rnd.next(100) > 95) {
        v[0] = 1;
        v[1] = 1000;
        v[2] = rnd.next(0, 1) ? 1 : 1000;
        v[3] = rnd.next(0, 1) ? 1 : 1000;
        println(v);
        return 0;
    }

    if (rnd.next(0,1)) {
        v[0] = rnd.next(1, 1000);
        v[1] = rnd.next(v[0] + 1, 1000);
        v[2] = rnd.next(1, 1000);
        int r = rnd.next(100);
        if (r > 25) {
            v[3] = v[1] - v[0] - v[2];
        } else if (r > 50) {
            v[3] = v[1] - v[0] + v[2];
        } else if (r > 75) {
            v[3] = v[0] - v[2] - v[1];
        } else {
            v[3] = v[0] + v[2] - v[1];
        }
        v[3] = abs(v[3]);
        println(v);
    } else {
        for (auto &e:v) e = rnd.next(1, 1000);
        if (v[0] > v[1]) swap(v[0], v[1]);
        else if (v[0] == v[1]) v[1]++;
        println(v);
    }

}
