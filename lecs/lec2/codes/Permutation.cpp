#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ld = long double;

#define sz(v) (int)v.size()
#define eb emplace_back
#define all(v) v.begin(),v.end()

const int n = 3;

vector<int> permutation;
bool was[n + 1];

void search() {
    if((int)permutation.size() == n) {
        for(auto e:permutation) cout<<e<<' ';
        cout<<'\n';
        return;
    }
    
    for(int i = 1; i <= n; i++) if(!was[i]) {
        was[i] = true;
        permutation.eb(i);
        search();
        permutation.pop_back();
        was[i] = false;
    }
} 

int main() {
    search();
    
    cout << '\n';

    vector<int> v = {3, 1, 2};
    
    do { //вектор v должен быть отсортирован
        for(auto e:v) cout<<e<<' ';
        cout<<'\n';
    } while(next_permutation(all(v))); // bool true false

    return 0;
}