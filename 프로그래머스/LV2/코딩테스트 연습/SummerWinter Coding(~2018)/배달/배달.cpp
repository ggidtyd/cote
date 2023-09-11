#include <iostream>
#include <vector>
#include <deque>
#include <unordered_map>
using namespace std;

int solution(int N, vector<vector<int> > road, int K) {
    int answer = 0, city1, city2, time, cur_city;
    unordered_map<int, vector<pair<int, int>>> map;
    vector<int> times(N + 1, 5000001);
    deque<pair<int, int>> q = { make_pair(1,0) };

    for (vector<int> data : road) {
        city1 = data[0], city2 = data[1], time = data[2];
        if (map.find(city1) == map.end()) {
            vector<pair<int, int>> vec = { make_pair(city2, time) };
            map.insert({ city1, vec });
        }
        else map[city1].push_back(make_pair(city2, time));

        if (map.find(city2) == map.end()) {
            vector<pair<int, int>> vec = { make_pair(city1, time) };
            map.insert({ city2, vec });
        }
        else map[city2].push_back(make_pair(city1, time));
    }

    while (!q.empty()) {
        cur_city = q.front().first, time = q.front().second;
        q.pop_front();

        times[cur_city] = min(times[cur_city], time);

        vector<pair<int, int>> connections = map[cur_city];
        for (pair<int, int> connection : connections) {
            int city = connection.first, t = connection.second;
            if (times[city] < time)continue;
            if (time + t > K)continue;
            q.push_back(make_pair(city, time + t));
        }
    }

    for (int t : times)
        if (t <= K)answer++;
    return answer;
}