#include <vector>
#include <queue>

using namespace std;
typedef priority_queue<int, vector<int>, greater<int>> HEAP;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    int temp = 0;
	
    HEAP heap(scoville.begin(), scoville.end());

    int heap_size = scoville.size();

    while (heap_size > 1) {
        temp = heap.top();
        heap.pop();
        heap.push(temp + heap.top() * 2);
        heap.pop();

        answer++;
        heap_size--;

        if (heap.top() >= K)
            return answer;
    }
    if (heap.top() < K)
        answer = -1;
    return answer;
}