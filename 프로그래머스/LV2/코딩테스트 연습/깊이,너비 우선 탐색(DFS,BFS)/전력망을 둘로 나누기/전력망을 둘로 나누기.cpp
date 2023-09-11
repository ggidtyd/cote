#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std;

void go(int tower, vector<vector<int>>& wires, set<int>& visit, vector<int> first_wire) {
    if(visit.find(tower) != visit.end())return;
    visit.insert(tower);

    for(vector<int> wire : wires) {
        if(wire == first_wire)continue;
        auto it = find(wire.begin(), wire.end(), tower);
        if(it != wire.end()) {
            int next = it - wire.begin() ? wire[0] : wire[1];
            go(next, wires, visit, first_wire);
        }
    }
}

int solution(int n, vector<vector<int>> wires) {
    int ans = 101;
    for(vector<int> wire : wires) {
        set<int> left, right;
        go(wire[0], wires, left, wire);
        go(wire[1], wires, right, wire);
        ans = min(ans, abs((int)left.size() - (int)right.size()));
    }
    return ans;
}