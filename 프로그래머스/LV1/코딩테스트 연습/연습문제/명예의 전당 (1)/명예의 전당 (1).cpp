#include <vector>
#include <queue>
using namespace std;
typedef priority_queue<int, vector<int>, greater<int>> HEAP;
vector<int> solution(int k, vector<int> score) {
    vector<int> answer, hall_of_fame;
    HEAP heap(hall_of_fame.begin(), hall_of_fame.end());

    for(int s : score) {
        heap.push(s);
        if(heap.size() > k)heap.pop();
        answer.push_back(heap.top());
    }
    return answer;
}