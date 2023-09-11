#include <string>
#include <vector>
using namespace std;

long long factorial(long long n) {
    return n <= 1 ? 1 : n * factorial(n - 1);
}

vector<int> solution(int n, long long k) {
    vector<int> answer, numbers;
    vector<long long> units;
    int number_idx = 0;
    int unit_idx = n - 1;
    long long cnt = 0;
    for (int x = 1; x <= n; x++)numbers.push_back(x);
    for (int x = 0; x < n; x++)units.push_back(factorial(x));

    while (unit_idx > 0) {
        cnt += units[unit_idx];
        if (cnt >= k) {
            answer.push_back(numbers[number_idx]);
            numbers.erase(numbers.begin()+number_idx);
            cnt -= units[unit_idx];
            unit_idx--;
            number_idx = 0;
        }
        else number_idx++;
    }
    answer.push_back(numbers[number_idx]);
    return answer;
}