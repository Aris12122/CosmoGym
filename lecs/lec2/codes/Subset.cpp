#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ld = long double;

vector<int> subset;

void search(int k,int n) {
    if(k == n + 1) {
        for(auto e:subset) cout<<e<<' ';
        cout<<'\n';
        return;
    }
    subset.emplace_back(k);
    search(k+1, n);

    subset.pop_back();
    search(k+1, n);
}

int main() {
    search(1,3);
    return 0;
}