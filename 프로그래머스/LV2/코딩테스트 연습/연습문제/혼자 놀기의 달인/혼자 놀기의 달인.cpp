#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int go(vector<int>& cards, int idx, vector<bool>& open, int cnt) {
    int ret = 0;
    if (open[idx])return cnt;

    open[idx] = true;
    ret = go(cards, cards[idx] - 1, open, cnt+1);

    return ret;
}

int solution(vector<int> cards) {
    int answer = 0;
    vector<int> result;
    vector<bool> open(cards.size(), false);

    for (int i = 0; i < cards.size(); i++) {
        if (open[i])continue;
        result.push_back(go(cards, i, open, 0));
    }

    sort(result.begin(), result.end());

    if (result.size() == 1)
        return 0;

    return result[0] * result[1];
}