#include <string>
#include <vector>
#include <queue>
using namespace std;

string solution(vector<string> cards1, vector<string> cards2, vector<string> goal) {
    queue<string> q1, q2;
    for (string c : cards1) q1.push(c);
    for (string c : cards2) q2.push(c);
    int goalIdx = 0;

    while (!q1.empty() || !q2.empty()) {
        if (goalIdx == goal.size()) break;

        if (!q1.empty() && q1.front() == goal[goalIdx]) {
            q1.pop();
            goalIdx++;
        }
        else if (!q2.empty() && q2.front() == goal[goalIdx]) {
            q2.pop();
            goalIdx++;
        }
        else break;
    }

    return goalIdx == goal.size() ? "Yes" : "No";
}