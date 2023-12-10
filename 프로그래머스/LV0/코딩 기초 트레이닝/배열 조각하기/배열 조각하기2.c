#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// arr_len은 배열 arr의 길이입니다.
// query_len은 배열 query의 길이입니다.
int* solution(int arr[], size_t arrLen, int query[], size_t queryLen) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int s = 0, e = arrLen;
    for(int i = 0; i < queryLen; i++)
        if(i % 2 != 0)
            s += query[i];
        else
            e = s + query[i] + 1;

    int* answer = (int*)malloc(sizeof(int) * (e - s));
    memcpy(answer, arr + s, sizeof(int) * (e - s));
    return answer;
}
