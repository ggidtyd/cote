#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// arr_len은 배열 arr의 길이입니다.
int solution(int arr[], size_t arrLen, int idx) {
    int answer = -1;
    
    for(int i = idx; i < arrLen; i++) {
        if(arr[i] == 1) {
            answer = i;
            break;
        }
    }
    
    return answer;
}