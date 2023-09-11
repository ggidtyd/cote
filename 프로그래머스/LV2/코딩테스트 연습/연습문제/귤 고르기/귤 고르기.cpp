#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

bool compare(pair<int, int> arg1, pair<int, int> arg2) {
    return arg2.second < arg1.second;
}

int solution(int k, vector<int> tangerine) {
    int answer = 0;
    unordered_map<int, int> map;

    for (int i : tangerine)map.insert({ i,0 });
    for (int i : tangerine)map[i]++;

    vector<pair<int, int>> vec(map.begin(), map.end());
    sort(vec.begin(), vec.end(), compare);

    for (auto p : vec) {
        k -= p.second;
        answer++;
        if (k <= 0)break;
    }

    return answer;
}