#include <string>
#include <vector>
#include <deque>
#include <algorithm>
using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    sort(people.begin(), people.end());

    deque<int> q(people.begin(), people.end());

    while (q.size() > 1) {
        if(q.front() + q.back() <= limit) {
            q.pop_front();
            q.pop_back();
        }
        else {
            q.pop_back();
        }
        answer++;
    }

    if(q.size())answer++;

    return answer;
}