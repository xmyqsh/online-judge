#include <iostream>

#define MOD 1000000007

using namespace std;

int dp[2][10] = {0};

int N, K;

int main() {
    cin >> N >> K;
    for (int i = 1; i <= min(K, 9); ++i)
        dp[0][i] = 1;
    for (int i = 1; i != N; ++i) {
        for (int j = 0; j <= min(K, 9); ++j) {
            dp[i & 1][j] = 0;
            for (int k = 0; k <= min(K, 9); ++k) {
                if (j * k > K) continue;
                dp[i & 1][j] = (dp[i & 1][j] + dp[(i - 1) & 1][k]) % MOD;
            }
        }
    }
    int result = 0;
    for (int i = 0; i <= min(K, 9); ++i) {
        result = (result + dp[(N - 1) & 1][i]) % MOD;
    }

    cout << result << endl;

    return 0;
}
