#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int num, int total) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(num * sizeof(int));
    int ansIdx = 0;
    int s = total / num;
    int e = total / num + num / 2;
    s -= num % 2 == 0 ? (num / 2 - 1) : num / 2;
    
    for(int i = s; i <= e; i++)
        answer[ansIdx++] = i;
    
    return answer;
}