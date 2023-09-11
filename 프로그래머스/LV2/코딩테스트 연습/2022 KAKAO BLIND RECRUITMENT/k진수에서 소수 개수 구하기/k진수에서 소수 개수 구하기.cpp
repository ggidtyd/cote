#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <cmath>
using namespace std;

bool ipn(long x) {
    if (x == 1)return false;
    for (long i = 2; i < long(pow(x, 0.5)) + 1; i++)
        if (x % i == 0)return false;
    return true;
}

vector<string> split(string str, char Delimiter) {
    istringstream iss(str);
    string buffer;

    vector<string> result;

    while (getline(iss, buffer, Delimiter))
        result.push_back(buffer);

    return result;
}

string to_k(int n, int k) {
    string s = "";
    int r = 0;
    while (n) {
        r = n % k;
        n = n / k;
        s += to_string(r);
    }
    reverse(s.begin(), s.end());
    return s;
}

int solution(int n, int k) {
    int answer = 0;
    string kstr = to_k(n, k);
    vector<string> by_0;
    if (kstr.find('0') == std::string::npos)
        return ipn(stol(kstr)) ? 1 : 0;

    by_0 = split(kstr, '0');

    for (string s : by_0) {
        if (s == "" || !ipn(stol(s)))continue;
        answer++;
    }
    return answer;
}