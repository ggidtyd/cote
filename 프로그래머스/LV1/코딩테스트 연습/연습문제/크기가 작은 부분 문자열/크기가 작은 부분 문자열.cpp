#include <string>
#include <vector>

using namespace std;

int solution(string t, string p) {
    int answer = 0;
    int p_len = p.length();
    long pl = stol(p);
    for (size_t i = 0; i <= t.length() - p_len; i++) {
        if(stol(t.substr(i, p_len)) <= pl)answer++;
    }
    return answer;
}