#include <vector>
#include <algorithm>
using namespace std;

bool cmp(pair<int, float> a, pair<int, float> b) {
    if (a.second == b.second)
        return a.first < b.first;
    else
        return a.second > b.second;
}

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;

    vector<pair<int, float>> vec;
    int u, d = 0;

    d = (int)stages.size();

    for (int n = 1; n <= N; n++) {
        u = (int)count(stages.begin(), stages.end(), n);
        if (u == 0) {
            vec.push_back(make_pair(n, 0));
        }
        else {
            vec.push_back(make_pair(n, (float)u / d));
        }
        d -= u;
    }

    sort(vec.begin(), vec.end(), cmp);

    for (auto& it : vec) {
        answer.push_back(it.first);
    }
    return answer;
}