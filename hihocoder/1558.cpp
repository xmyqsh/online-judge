#include <iostream>
#include <vector>

using namespace std;

int N, K;
int path[10];

void dfs(int cur, int cnt) {
    if (cnt == N) {
        for (int i = 0; i != N; ++i)
            cout << path[i];
        cout << endl;
        return;
    }
    for (int i = 0; i <= K; ++i) {
        if (cur * i > K) break;
        path[cnt] = i;
        dfs(i, cnt + 1);
    }
}

int main() {
    cin >> N >> K;
    for (int i = 1; i <= K; ++i) {
        path[0] = i;
        dfs(i, 1);
    }
    return 0;
}
