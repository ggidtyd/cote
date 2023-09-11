#include <string>
#include <vector>

using namespace std;

vector<int> ans(11, 0);
int max_diff = 0;

bool check_low_score(vector<int>& lion) {
    for(int i = 10; i >= 0; i--) {
        if(lion[i] > ans[i])return true;
        else if(lion[i] < ans[i])return false;
    }
}

void go(int idx, int n, vector<int>& apeach, vector<int>& lion) {
    if(idx == 11 || n < 0)return;

    if(idx == 10 && n >= 0) {
        lion[idx] = n;

        int lion_score = 0;
        int apeach_score = 0;

        for(int i = 0; i <= 10; i++) {
            if(lion[i] > apeach[i]) lion_score += 10-i;
            else if(apeach[i] != 0) apeach_score += 10-i;
        }

        int diff = lion_score - apeach_score;
        if(diff > max_diff) {
            max_diff = diff;
            copy(lion.begin(), lion.end(), ans.begin());
        }
        else if(diff == max_diff) {
            if(check_low_score(lion))
                copy(lion.begin(), lion.end(), ans.begin());
        }
        return;
    }

    lion[idx] += apeach[idx]+1;
    go(idx+1, n-(apeach[idx]+1), apeach, lion);
    lion[idx] = 0;
    go(idx+1, n, apeach, lion);
}

vector<int> solution(int n, vector<int> info) {
    vector<int> lion(11,0);
    go(0, n, info, lion);
    if(!max_diff)ans = {-1};
    return ans;
}