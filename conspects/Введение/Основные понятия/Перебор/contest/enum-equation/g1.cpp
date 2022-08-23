#include "testlib.h"
#include <bits/stdc++.h>
 
using namespace std;
 
#define forn(i, n) for (int i = 0; i < int(n); i++)
#define sz(v) (int)v.size()

const int N = (int)1e6;
 
int main(int argc, char* argv[]) {
    registerGen(argc, argv, 1);

    int x1 = opt<int>(1);
    int x2 = opt<int>(2);
    int x3 = opt<int>(3);

    int K = opt<int>(4);

    int B = -x3 - x1 - x2;
    int C = x2 * x3 + x1 * x3 + x1 * x2;
    int D = -x1 * x2 * x3;
    
    long long A = rnd.next(-K, K);
    while(A == 0) A = rnd.next(-K, K);

    if (max({abs(B), abs(C), abs(D)}) * abs(A) > N) {
        A = rnd.next(-100, 100);
        while(A == 0) A = rnd.next(-K, K);
    }

    if (max({abs(B), abs(C), abs(D)}) * abs(A) > N) {
        A = 1;
    }

    B *= A;
    C *= A;
    D *= A;

    println(A, B, C, D);
}


// a*(x - x1)*(x - x2)*(x - x3) = a * x^3 + x^2 * (-x3 - x1 - x2) + x(x2x3 + x1x3 + x1x2) - x1x2x3