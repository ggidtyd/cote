#include <vector>
#include <string>
#include<algorithm>
#include <map>

#define number_cnt pair<string, int>

using namespace std;

bool cmp(number_cnt& p1, number_cnt& p2) {
    return p2.second < p1.second;

}

vector<int> solution(string s) {
    string number;
    vector<int> answer;
    map<string, int> number_cnt_map;
    for (char c : s) {
        if (isdigit(c))number += c;
        else {
            if (number == "")continue;
            if (number_cnt_map.find(number) == number_cnt_map.end()) number_cnt_map[number] = 1;
            else number_cnt_map[number]++;
            number = "";
        }
    }
    vector<number_cnt> number_cnt_vec(number_cnt_map.begin(), number_cnt_map.end());
    sort(number_cnt_vec.begin(), number_cnt_vec.end(), cmp);
    for (number_cnt nc : number_cnt_vec)answer.push_back(stoi(nc.first));
    return answer;
}