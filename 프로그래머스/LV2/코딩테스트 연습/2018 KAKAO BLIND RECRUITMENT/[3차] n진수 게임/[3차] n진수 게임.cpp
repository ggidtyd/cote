#include <string>
#include <vector>

using namespace std;

string to_n(int i, int n) {
    string s = "";
    char r;

    while (i) {
        r = i % n;
        i = i / n;
        if(i >= 10 && i <= 15)s += (char)(r+55);
        else s += (char)r;
    }

    reverse(s.begin(), s.end());
    return s;
}

string solution(int n, int t, int m, int p) {
    string answer = "";
    string s = "0";

    int i = 1;
    while (s.length() < t*m) {
        s += to_n(i,n);
        i++;
    }
    
    i = p-1;
    while (t) {
        answer += s[i];
        i += m;
        t--;
    }
    
    return answer;
}