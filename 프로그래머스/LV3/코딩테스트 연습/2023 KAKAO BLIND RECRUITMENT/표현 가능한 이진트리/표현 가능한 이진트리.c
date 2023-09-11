#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

int check(long long n, int l){
    if(n == 0 || l == 1)
        return 1;

    int mid = l / 2;
    long long left = ((1 << mid) - 1) & (n >> (mid + 1));
    long long right = ((1 << mid) - 1) & n;

    if (((n >> mid) & 1) && check(left, mid) && check(right, mid))
        return 1;
    return 0;
}


// numbers_len은 배열 numbers의 길이입니다.
int* solution(long long numbers[], size_t numbersLen) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(sizeof(int) * numbersLen);
    int bLen = 0, h = 0, totalLen = 0;

    for(int i = 0; i < numbersLen; i++){
        bLen = (int)floor(log2(numbers[i])) + 1;
        h = (int)floor(log2(bLen)+1);
        totalLen = (1 << h) - 1;
        answer[i] = check(numbers[i], totalLen);
    }
    return answer;
}