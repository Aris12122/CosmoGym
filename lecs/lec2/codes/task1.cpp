#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ld = long double;

#define sz(v) (int)v.size()
#define eb emplace_back
#define all(v) v.begin(),v.end()


const int n = 8;
bool col[n+1], diag1[2*n + 1], diag2[2*n + 1];

int cnt = 0;

void search(int x) {
    if(x == n+1) {
        cnt++;
        return;
    }
    
    for(int y = 1; y <= n; y++) {
        if(col[y] || diag1[x+y] || diag2[x-y+n]) continue;
        col[y] = diag1[x+y] = diag2[x-y+n] = 1;
        search(x + 1);
        col[y] = diag1[x+y] = diag2[x-y+n] = 0;
    }
}

int main() {
    search(1);
    cout << cnt;

    return 0;
}