#include <string>
#include <vector>
#include <set>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    vector<int> answer = {0,0};
    set<string> used;
    string before = words[0];
    used.insert(words[0]);

    for(int i = 0; i < words.size(); i++) {
        if(before.back() != words[i][0] || used.find(words[i]) != used.end()) {
            answer[0] = i%n+1;
            answer[1] = i/n+1;
            break;
        }
        used.insert(words[i]);
        before = words[i];
    }
    return answer;
}