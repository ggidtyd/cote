#include <string>
#include <vector>

using namespace std;

string answer = "";

void go(char before, string s, int s_idx, int s_len) {
    if(s_idx == s_len)return;

    if(isdigit(before))answer += tolower(s[s_idx]);
    else if(before == ' ')answer += toupper(s[s_idx]);
    else answer += tolower(s[s_idx]);

    go(s[s_idx], s, s_idx+1, s_len);

}

string solution(string s) {
    answer = isalpha(s[0]) ? toupper(s[0]) : s[0];
    go(s[0], s, 1, s.length());
    return answer;
}