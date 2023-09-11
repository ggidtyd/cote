#include <string>
#include <vector>
#include <stack>
#define idx_price pair<int,int>
using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;
    stack<idx_price> stack;
    int idx;
    for(int i = prices.size()-1; i >= 0; i--)answer.push_back(i);

    for(int i = 0; i < prices.size(); i++) {
        while (!stack.empty() && stack.top().second > prices[i]) {
            idx = stack.top().first;
            answer[idx] = i - idx;
            stack.pop();
        }
        stack.push(idx_price(i, prices[i]));
    }
    return answer;
}