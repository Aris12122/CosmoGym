#include "testlib.h"
#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)

int v[4];

bool readAnswer(InStream& in) {
    string ans_s = in.readLine();
    if (ans_s == "No solution") {
        return false;
    }
    in.quitif(ans_s.empty(), _pe, "Expected No solution or number");
    for (auto &e:ans_s) {
        in.quitif(!isdigit(e), _pe, "Expected No solution or number");
    }
    int ans = stoi(ans_s);
    int a = v[0], b = v[1], c = v[2], d = v[3];
    if ((a + c == b + d || a+c == b - d) && ans == a+c) return true;
    else if(b + d == a-c && b + d == ans) return true;
    else if(b-d >=0 && a-c == b-d && ans == b-d) return true;
    in.quitf(_wa, "Wrong answer");
}

int main(int argc, char* argv[]) {
    registerTestlibCmd(argc, argv);

    for (auto &e:v) {
        e = inf.readInt();
    }

    bool ja = readAnswer(ans);
    bool pa = readAnswer(ouf);
    
    if (ja != pa) {
        if (pa)
            quitf(_fail, "Participant has answer, but jury doesn't");
        if (ja)
            quitf(_wa, "Jury has answer, but participant doesn't");
    }
    quitf(_ok, "OK");
}
