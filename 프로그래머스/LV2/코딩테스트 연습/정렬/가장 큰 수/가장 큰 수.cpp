#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool compare(string arg1, string arg2) {
    return arg1 + arg2 > arg2 + arg1;
}

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> numbers_str;

    for (int number : numbers)
        numbers_str.push_back(to_string(number));

    sort(numbers_str.begin(), numbers_str.end(), compare);

    for (string number : numbers_str)
        answer += number;
    
    if(answer[0] == '0')
        answer = "0";
    
    return answer;
}