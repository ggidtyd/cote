#include <string>
#include <vector>

using namespace std;

int count_1(int n) {
    int cnt = 0;
    while (n) {
        if(n & 1)cnt++;
        n >>= 1;
    }
    return cnt;
}

int solution(int n) {
    int n_cnt = count_1(n);
    while (true) {
        if(count_1(n+1) == n_cnt)return n+1;
        n++;
    }
}