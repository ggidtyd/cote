#include <string>
#include <vector>

using namespace std;

string solution(string number, int k) {
    string answer = "";

    for(char n : number) {
        while (answer != "" && k > 0 && answer.back() < n) {
            answer.pop_back();
            k -= 1;
        }
        answer.push_back(n);
    }

    if(k)return answer.substr(0, answer.length()-k);
    
    return answer;
}