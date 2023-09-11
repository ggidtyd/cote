#include <string>
#include <vector>
using namespace std;

int ans = 0;

void go(vector<bool> visit, vector<vector<int>>& dungeons, int k, int n) {
    if(n > ans)ans = n;

    for(int i = 0; i < dungeons.size(); i++) {
        if(!visit[i] && k >= dungeons[i][0]) {
            visit[i] = true;
            go(visit, dungeons, k-dungeons[i][1], n+1);
            visit[i] = false;
        }
    }
}

int solution(int k, vector<vector<int>> dungeons) {
    vector<bool> visit;
    for(int i = 0; i < dungeons.size(); i++)visit.push_back(false);
    go(visit, dungeons, k, 0);
    return ans;
}