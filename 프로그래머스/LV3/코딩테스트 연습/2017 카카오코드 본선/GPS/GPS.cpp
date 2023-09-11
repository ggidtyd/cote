#include <map>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

#define MAX 201

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int n, int m, vector<vector<int>> edge_list, int k, vector<int> gps_log) {
    vector<vector<int>> dp(k, vector<int>(n + 1, MAX));
    map<int, vector<int>> graph;

    for (auto v : edge_list) {
        graph[v[0]].push_back(v[1]);
        graph[v[1]].push_back(v[0]);
    }

    dp[0][gps_log[0]] = 0;

    for (int i = 1; i < k; i++) {
        for (int j = 1; j <= n; j++) {
            dp[i][j] = min(dp[i - 1][j], dp[i][j]);
            for (int adj : graph[j])
                dp[i][j] = min(dp[i - 1][adj], dp[i][j]);

            dp[i][j] += (gps_log[i] == j) ? 0 : 1;
        }
    }

    if (dp[k - 1][gps_log[k - 1]] >= MAX)
        return -1;

    return dp[k - 1][gps_log[k - 1]];
}

int main() {
    vector<vector<int>> edge_list = {{1, 2}, {1, 3}, {2, 3}, {2, 4}, {3, 4}, {3, 5}, {4, 6}, {5, 6}, {5, 7}, {6, 7}};
    vector<int> gps_log = {1, 2, 3, 3, 6, 7};
    cout << solution(7, 10, edge_list, 6, gps_log) << endl;
    return 0;
}