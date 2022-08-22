#include "testlib.h"
#include <sstream>

using namespace std;

int n;
long long m;

vector<int> f;

void add(int k) {
    for (; k <= n; k += k&-k) {
        f[k]++;
    }
}

int sum(int k) {
    int res = 0;
    for (; k > 0; k -= k&-k) {
        res += f[k];
    }
    return res;
}

long long readAnswer(InStream& in) {
    vector<int> a = in.readInts(n, 1, n, "Перестановка");
    in.quitif(n != (set<int>(a.begin(),a.end())).size(), _wa, "Ожидается перестановка");
    f.resize(n + 1, 0);
    long long res = 0;
    for (int i = 0; i < n; i++) {
        int x = a[i];
        res += i - sum(x);
        add(x);
    }
    f.clear();
    return res;
}

int main(int argc, char * argv[])
{
    registerTestlibCmd(argc, argv);

    n = inf.readInt();
    m = inf.readLong();

    long long ja = readAnswer(ans);
    long long pa = readAnswer(ouf);

    quitif(ja != m, _fail, "Количество инверсий ожидается ровно %lld, получено: %lld", m, ja);
    quitif(pa != m, _wa, "Количество инверсий должно быть ровно %lld, ваша перестановка имеет: %lld", m, pa);

    quitf(_ok, "res = %d", ja);
    return 0;
}