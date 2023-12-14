#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// arr_len은 배열 arr의 길이입니다.
int* solution(int arr[], size_t arrLen) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int first2 = 0, last2 = 0, ansIdx = 0;
    int* answer = (int*)malloc(sizeof(int) * arrLen);
    
    for(int i = 0; i < arrLen; i++) {
        if(arr[i] == 2) {
            first2 = i;
            break;
        }
    }
    
    for(int i = arrLen - 1; i >= 0; i--) {
        if(arr[i] == 2) {
            last2 = i;
            break;
        }
    }
    
    if(first2 == 0 && last2 == 0)
        answer[0] = -1;
    else
        memcpy(answer, arr + first2, sizeof(int) * (last2 - (first2 - 1)));
    answer = realloc(answer, sizeof(int) * (last2 - (first2 - 1)));
    
    return answer;
}