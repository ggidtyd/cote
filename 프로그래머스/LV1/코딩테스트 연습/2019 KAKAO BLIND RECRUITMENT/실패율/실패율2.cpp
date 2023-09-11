#include <vector>
#include <algorithm>
#include <map>

using namespace std;

bool cmp(pair<int, float> a, pair<int, float> b) {
    if (a.second == b.second)
        return a.first < b.first;
    else
        return a.second > b.second;
}

vector<int> sortMapByValue(map<int, float>& map) {
    vector<pair<int, float>> vec;
    vector<int> ret;

    for (auto& it : map) {
        vec.push_back(it);
    }

    sort(vec.begin(), vec.end(), cmp);

    for (auto& it : vec) {
        ret.push_back(it.first);
    }
    return ret;
}

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;

    map<int, float> stageNumberFailureRateMap;
    int u, d = 0;

    d = stages.size();
    for (int n = 1; n <= N; n++) {
        u = count(stages.begin(), stages.end(), n);
        if (u == 0) {
            stageNumberFailureRateMap[n] = 0;
        }
        else {
            stageNumberFailureRateMap[n] = (float)u / d;
        }
        d -= u;
    }

    answer = sortMapByValue(stageNumberFailureRateMap);
    return answer;
}
