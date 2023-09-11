#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    unordered_map<string, int> map;

    for(vector<string> clothe : clothes) {
        if(map.find(clothe[1]) == map.end())map.insert({make_pair(clothe[1], 1)});
        else map[clothe[1]]++;
    }

    for(auto it : map)
        answer *= it.second+1;

    return answer-1;
}