#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <sstream>

using namespace std;

const string ALL = "-";
unordered_map<string, vector<int>> queries_derived_from_info;

void get_queries_derived_from_info(string* input_info, int all_mask, int score) {
    string q = "";
    for (int i = 0; i < 4; i++)
        q += (all_mask & (1 << i)) ? ALL : input_info[i];
    queries_derived_from_info[q].push_back(score);
}

vector<int> solution(vector<string> info, vector<string> query) {
    vector<int> answer;
    string input_info[4], tmp;
    int score;

    for (auto& inf : info) {
        istringstream iss(inf);
        iss >> input_info[0] >> input_info[1] >> input_info[2] >> input_info[3] >> score;
        for (int i = 0; i < 16; i++) get_queries_derived_from_info(input_info, i, score);
    }

    for (auto& aqdfi : queries_derived_from_info) sort(aqdfi.second.begin(), aqdfi.second.end());

    for (auto& que : query) {
        istringstream iss(que);
        iss >> input_info[0] >> tmp >> input_info[1] >> tmp >> input_info[2] >> tmp >> input_info[3] >> score;
        string q = input_info[0] + input_info[1] + input_info[2] + input_info[3];
        
        answer.push_back(queries_derived_from_info[q].end() - lower_bound(queries_derived_from_info[q].begin(), queries_derived_from_info[q].end(), score));
    }
    return answer;
}