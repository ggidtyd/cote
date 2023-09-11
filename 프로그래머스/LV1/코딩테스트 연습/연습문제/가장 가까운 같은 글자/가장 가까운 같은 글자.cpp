#include <string>
#include <vector>
#include <map>
using namespace std;

vector<int> solution(string s) {
    map<char,vector<int>> alphabet_idxs_map;
    vector<int> v;
    vector<int> answer;

    for(int i = 0; i < s.length(); i++) {
        if(alphabet_idxs_map.find(s[i]) == alphabet_idxs_map.end()) {
            v = {i};
            alphabet_idxs_map.insert(make_pair(s[i], v));
            answer.push_back(-1);
        }
        else {
            answer.push_back(i - alphabet_idxs_map[s[i]].back());
            alphabet_idxs_map[s[i]].push_back(i);
        }
    }
    return answer;
}