#include <string>
#include <vector>
#include <stack>

using namespace std;

int solution(vector<int> order) {
    int answer = 0;
    stack<int> stack;

    for(int i = 1; i <= order.size(); i++) {
        stack.push(i);
        while (stack.top() == order[answer]) {
            answer++;
            stack.pop();
            if(stack.size() == 0)break;
        }
    }
    return answer;
}