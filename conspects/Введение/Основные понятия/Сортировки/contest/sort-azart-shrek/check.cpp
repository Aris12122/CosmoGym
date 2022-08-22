#include "testlib.h"
#include <sstream>

using namespace std;

int n;
vector<int> a;

int readAnswer(InStream& in) {
    int m = n / 2;
    vector<int> v = in.readInts(m, 1, n, "Номера карточек, которые выбирает Шрек");
    in.quitif(m != int(set<int>(v.begin(), v.end()).size()), _wa, "Номера карточек должны быть различны");
    int res = 0;
    for (int i = 0; i < m; i++) {
        res += a[v[i] - 1];
    }
    return res;
}

int main(int argc, char * argv[])
{
    registerTestlibCmd(argc, argv);

    n = inf.readInt();
    a = inf.readInts(n);

    int ja = readAnswer(ans);
    int pa = readAnswer(ouf);

    if (ja != pa) {
        if (ja < pa) {
            quitf(_wa, "Это не максимальный возможный выигрыш");
        } else {
            quitf(_fail, "Участник имеет лучший ответ");
        }
    }

    quitf(_ok, "res = %d", ja);
    return 0;
}