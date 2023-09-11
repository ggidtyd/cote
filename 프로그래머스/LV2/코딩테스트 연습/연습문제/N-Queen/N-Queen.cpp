#include <string>
#include <vector>

using namespace std;
bool in_attack_range_col[24] = {false,};
bool in_attack_range_d1[24] = {false,};
bool in_attack_range_d2[24] = {false,};

int go(int row, int n) {
    int answer = 0;
    int d1, d2;
    if(row==n)return 1;

    for(int i = 0; i < n; i++) {
        d1 = row + i;
        d2 = n + row - i;
        if(!in_attack_range_col[i] && !in_attack_range_d1[d1] && !in_attack_range_d2[d2]) {
            in_attack_range_col[i] = true;
            in_attack_range_d1[d1] = true;
            in_attack_range_d2[d2] = true;
            answer += go(row+1, n);
            in_attack_range_col[i] = false;
            in_attack_range_d1[d1] = false;
            in_attack_range_d2[d2] = false;            
        }
    }
    return answer;
}

int solution(int n) {
    return go(0,n);
}