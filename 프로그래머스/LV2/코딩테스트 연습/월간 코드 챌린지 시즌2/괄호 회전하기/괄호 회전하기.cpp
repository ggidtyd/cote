#include <string>
#include <vector>
#include <stack>
using namespace std;

int solution(string s) {
    int answer = 0;
    int s_len = s.length();
    string temp;
    stack<char> stack;
    s += s;

    for (int i = 0; i < s_len; i++) {
        temp = s.substr(i, s_len);
        while (!stack.empty())
            stack.pop();

        for (char c : temp) {
            if (!stack.empty() && ((c - stack.top()) == 1 || (c - stack.top()) == 2)) stack.pop();
            else stack.push(c);
        }
        if (stack.empty())answer++;
    }
    return answer;
}