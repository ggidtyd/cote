#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
int ans = 0;

void go(int select, int sum, int j, int* number, size_t number_len) {
    if(select == 3) {
        if(sum == 0)ans++;
        return;
    }
    for(int i = j; i < number_len; i++) {
        go(select+1, sum+number[i], i+1, number, number_len);
    }
}

// number_len은 배열 number의 길이입니다.
int solution(int number[], size_t number_len)  {
    go(0,0,0,number,number_len);
    return ans;
}