#include <string>
#include <vector>
#include <regex>
using namespace std;

int solution(string skill, vector<string> skill_trees) {
    int answer = 0;
    for (string st : skill_trees) {
        st = regex_replace(st, regex("[^" + skill + "]+"), "");
        if (st == "" || st[0] == skill[0] && (skill.find(st) != string::npos))answer++;
    }
    return answer;
}