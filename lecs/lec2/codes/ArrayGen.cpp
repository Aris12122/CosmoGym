#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ld = long double;

mt19937 rng(58);
const int mod = 1e9;

int main(){
    ios::sync_with_stdio(0); cin.tie(0);
    int n; cin >> n;
    vector<int> v(n);
    for(int i = 0; i < n; i++) {
        v[i] = rng() % mod;
    }
    freopen("in.txt", "w", stdout);
    cout << n << '\n';
    for(auto e : v) cout << e << ' ';
    cout << '\n';
}
