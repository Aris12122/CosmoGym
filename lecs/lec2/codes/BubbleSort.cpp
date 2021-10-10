#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ld = long double;


int main() {
    int n; cin>>n;
    vector<int> v(n);
    for(auto &e:v) cin>>e;

    for(int i = 0; i < n; i++) {
        for(int j = 1; j < n; j++) {
            if(v[j-1] > v[j]) swap(v[j-1],v[j]);
        }
    }

    for(auto e:v) cout<<e<<' ';
    cout<<'\n';
    
    return 0;
}