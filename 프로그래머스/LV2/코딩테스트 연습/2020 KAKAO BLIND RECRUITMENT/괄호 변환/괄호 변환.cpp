#include <string>
#include <vector>
#include <stack>
using namespace std;

string flip(string u) {
    string ret = "";
    for (char c : u) {
        if (c == '(')ret += ")";
        else ret += "(";
    }
    return ret;
}

bool correct_parenthesis(string s) {
    stack<char> stack;
    for (char c : s) {
        if (!stack.empty() && stack.top() == '(' && c == ')')stack.pop();
        else stack.push(c);
    }
    return stack.empty() ? true : false;
}

string go(string w) {
    if (w == "")return "";

    int num_of_open = 0, num_of_close = 0;
    string s = "", u = "", v = "";

    for (int i = 0; i < w.length(); i++) {
        if (w[i] == '(')num_of_open++;
        else num_of_close++;

        if (num_of_open == num_of_close) {
            u = w.substr(0, i + 1);
            v = w.substr(i + 1);
            break;
        }
    }

    if (correct_parenthesis(u)) {
        u += go(v);
        return u;
    }
    else {
        s += "(" + go(v) + ")";
        u = u.substr(1, u.length()-2);
        s += flip(u);
        return s;
    }
}

string solution(string p) {
    if (correct_parenthesis(p))
        return p;

    return go(p);
}