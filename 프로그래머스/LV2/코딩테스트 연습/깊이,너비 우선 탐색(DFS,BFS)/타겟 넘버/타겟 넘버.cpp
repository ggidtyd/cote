#include <string>
#include <vector>

using namespace std;

int go(vector<int>& numbers, int target, int i, int s) {
    int ans = 0;
    if(i == numbers.size())return s == target ? 1: 0;

    ans += go(numbers, target, i+1, s+numbers[i]);
    ans += go(numbers, target, i+1, s-numbers[i]);
    return ans;
}

int solution(vector<int> numbers, int target) {
    return go(numbers, target, 0, 0);
}

