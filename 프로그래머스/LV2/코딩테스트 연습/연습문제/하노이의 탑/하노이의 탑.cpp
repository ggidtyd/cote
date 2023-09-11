#include <string>
#include <vector>

using namespace std;

void go(int from, int to, int n, vector<vector<int>>& ans) {
    if(n == 0)return;

    int other = 6 - (from+to);
    go(from, other, n-1, ans);
    vector<int> temp = {from, to};
    ans.push_back(temp);
    go(other, to, n-1, ans);
}

vector<vector<int>> solution(int n) {
    vector<vector<int>> answer;
    go(1,3,n,answer);
    return answer;
}