#include <iostream>
#include<string>
#include <stack>
using namespace std;

int solution(string s) {
    stack<int> stack;

    for(char c : s) {
        if(!stack.empty() && stack.top() == c)stack.pop();
        else stack.push(c);
    }
    return stack.empty() ? 1 : 0;
}