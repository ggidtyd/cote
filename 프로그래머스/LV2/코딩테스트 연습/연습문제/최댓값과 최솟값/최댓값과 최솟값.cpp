#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string solution(string s) {
    vector<int> vec;
    string temp = "";
    for (char c : s) {
        if (c == ' ') {
            vec.push_back(stoi(temp));
            temp = "";
        }
        else temp += c;
    }
    vec.push_back(stoi(temp));
    return to_string(*min_element(vec.begin(), vec.end())) + " " + to_string(*max_element(vec.begin(), vec.end()));
}