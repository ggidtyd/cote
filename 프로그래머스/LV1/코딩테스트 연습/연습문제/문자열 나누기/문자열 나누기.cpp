#include <string>

using namespace std;

int solution(string s) {
    int answer = 0;
    int x_cnt = 0;
    char x = 0;


    for (char c : s) {
        if (x == 0) {
            x = c;
            x_cnt = 1;
            continue;
        }

        x_cnt += x == c ? 1 : -1;

        if (x_cnt == 0) {
            answer++;
            x = 0;
        } 
    }
    if (x_cnt != 0)answer++;
    return answer;
}