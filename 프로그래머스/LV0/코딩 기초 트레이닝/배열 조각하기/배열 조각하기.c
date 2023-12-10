#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// arr_len은 배열 arr의 길이입니다.
// query_len은 배열 query의 길이입니다.
int* solution(int arr[], size_t arrLen, int query[], size_t queryLen) {
    int s = 0, e = s + arrLen - 1;
    
    for(int i = 0; i < queryLen; i++)
        if(i % 2 == 0)
            e = s + query[i];
        else
            s += query[i];
    
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc((e - (s - 1)) * sizeof(int));
    int ansIdx = 0;
    
    for(int i = s; i <= e; i++)
        answer[ansIdx++] = arr[i];
    
    return answer;
}