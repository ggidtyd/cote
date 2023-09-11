#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;

int solution(std::vector<int> a) {
    unordered_map<int, pair<int, int>> map;
    unordered_set<int> s(a.begin(), a.end());
    int c = 0;

    for(auto n : s)
        map.insert({n, make_pair(0, -1)});
    
    for(int i = 0; i < a.size(); i++) {
        if(i > 0 && map[a[i]].second != i-1 && a[i-1] != a[i]) {
            map[a[i]].first++;
            map[a[i]].second = i-1;
        } 
        else if(i < a.size()-1 && a[i] != a[i+1]) {
            map[a[i]].first++;
            map[a[i]].second = i+1;            
        }
        c = max(c, map[a[i]].first);
    }

    return a.size() >= c * 2 ? c * 2 : (a.size()-c) * 2;
}