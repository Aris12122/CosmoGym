#include "testlib.h"
#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)

int n, m;
vector<string> phones;
string s;

bool readAnswer(InStream& in) {
    int k = in.readInt(-1, m / 2, "k");
    if (k == -1)
        return false;
    if (k == 0)
        in.quitf(_wa, "k can't be 0");
    
    string t;
    forn(j, k) {
        int l = in.readInt(1, m, "l");
        int r = in.readInt(1, m, "r");
        int i = in.readInt(1, n, "i");

        t += phones[i-1].substr(l-1, r-l + 1);
    }
    if (t != s) {
        in.quitf(_wa, "Answer phone is not \"s\"");
    }
    return true;
}

int main(int argc, char* argv[]) {
    registerTestlibCmd(argc, argv);

    int t = inf.readInt();
    int sum_nm = 0;
    forn(tt, t) {
        setTestCase(tt + 1);
        n = inf.readInt();
        m = inf.readInt();
        inf.readEoln();
        sum_nm += n * m;

        phones.resize(n);
        forn(i, n)
            phones[i] = inf.readLine();
        s = inf.readLine();

        bool ja = readAnswer(ans);
        bool pa = readAnswer(ouf);
        
        if (ja != pa) {
            if (pa)
                quitf(_fail, "Participant has answer, but jury doesn't");
            if (ja)
                quitf(_wa, "Jury has answer, but participant doesn't");
        }
    }
    quitf(_ok, "sum_nm=%d", sum_nm);
}
