#include <string>
#include <vector>

using namespace std;

int go(vector<int>& numbers, int idx, int n, int s) {
    int ret = 0;

    if(s == n)
        return 1;

    if(s > n || idx == numbers.size())
        return 0;

    ret = go(numbers, idx+1, n, s+numbers[idx]);

    return ret;
}

int solution(int n) {
    int answer = 0;
    vector<int> numbers;
    for(int i = 1; i <= n; i++)numbers.push_back(i);

    for(int i = 0; i < n; i++)
        answer += go(numbers, i, n, 0);
    return answer;
}