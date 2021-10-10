#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ld = long double;

#define all(v) v.begin(),v.end()

const int INF = INT_MAX >> 1;

int main() {
    clock_t begin, end;
    begin = clock(); 

    int n; cin>>n;

    int n2;
    for(n2 = 1;n2 < n;n2 <<= 1); 
    
    vector<int> v(n);
    
    for(auto &e:v) cin>>e;
    // vector<int> check(v); sort(all(check));
    // cerr << n2 << endl;

    v.resize(n2,INF);

    for(int len = 1; len < n2; len *= 2) {
        vector<int> c(n2);
        int i = 0;
        for(int L = 0, R, tl, tr; L < n2; L = tr) {
            R = L + len;
            tl = L + len, tr = R + len;

            // cerr << L << ' ' << R << ' ' << tl << ' ' << tr << '\n';
            while(L < tl || R < tr) {
                if(R == tr || (L < tl ? v[L] < v[R] : false)) {
                    c[i++] = v[L++];
                } else {
                    c[i++] = v[R++];
                }
            }

            continue; //bonus
            merge(v.begin() + L,v.begin() + tl, v.begin() + R,v.begin() + tr, c.begin() + L);
        }
        /* for(auto e:c) cerr << e << ' ';
        cerr << endl;  */
        swap(v,c);
    }
    v.resize(n);
    
    end = clock();
    cout << "Time: " << ld(end - begin) / CLOCKS_PER_SEC << " seconds \n";
    
    return 0;
}