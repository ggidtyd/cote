#include <string>
#include <vector>
#include <unordered_map>
#include <sstream>
#include <numeric>
#include <algorithm>
#include <cmath>
#define data pair<vector<int>, string>
using namespace std;

bool compare(pair<int, data>& arg1, pair<int, data>& arg2) {
    return arg1.first < arg2.first;
}

vector<string> split(string str, char Delimiter) {
    istringstream iss(str);
    string buffer;

    vector<string> result;

    while (getline(iss, buffer, Delimiter))
        result.push_back(buffer);

    return result;
}

vector<int> solution(vector<int> fees, vector<string> records) {
    vector<int> answer;
    vector<string> _record, hm;
    unordered_map<int, data> map;
    unordered_map<int, data>::iterator iter;
    int last_time = 23 * 60 + 59;
    int time, car_number;
    string inout;

    for (string record : records) {
        _record = split(record, ' ');
        hm = split(_record[0], ':');
        time = stoi(hm[0]) * 60 + stoi(hm[1]);
        car_number = stoi(_record[1]);
        inout = _record[2];

        if (map.find(car_number) == map.end()) {
            vector<int> v = { -time };
            map.insert(make_pair(car_number, data(v, inout)));
        }
        else if (map[car_number].second == "IN") {
            map[car_number].first.push_back(time);
            map[car_number].second = inout;
        }
        else if (map[car_number].second == "OUT") {
            map[car_number].first.push_back(-time);
            map[car_number].second = inout;
        }
    }

    for (auto iter : map) {
        if (iter.second.second == "IN") {
            map[iter.first].first.push_back(last_time);
            map[iter.first].second = "OUT";
        }
    }

    vector<pair<int, data>> vec(map.begin(), map.end());
    sort(vec.begin(), vec.end(), compare);

    for (pair<int, data> info : vec) {
        int total_time = accumulate(info.second.first.begin(), info.second.first.end(), 0)-fees[0];
        if (total_time <= 0)answer.push_back(fees[1]);
        else answer.push_back(fees[1] + ceil((double)total_time / (double)fees[2]) *fees[3]);
    }

    return answer;
}