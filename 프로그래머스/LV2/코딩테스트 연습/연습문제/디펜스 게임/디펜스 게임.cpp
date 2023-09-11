#include <string>
#include <vector>
#include <queue>
using namespace std;

int solution(int n, int k, vector<int> enemy) {
    int sum = 0;
    priority_queue<int, vector<int>, greater<int>> min_heap;

    for(int i = 0; i < enemy.size(); i++) {
        min_heap.push(enemy[i]);

        if(min_heap.size() > k) {
            sum += min_heap.top();
            min_heap.pop();
        }

        if(sum > n)
            return i;
    }

    return enemy.size();
}