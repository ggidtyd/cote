#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// arr_len은 배열 arr의 길이입니다.
int* solution(int arr[], size_t arrLen, int k) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(k * sizeof(int));
    int ansIdx = 0;
    bool appearance[100001] = {false, };
    
    for(int i = 0; i < arrLen; i++) {
        if(ansIdx == k) break;
        if(appearance[arr[i]]) continue;
        
        appearance[arr[i]] = true;
        answer[ansIdx++] = arr[i];
    }
    
    while(ansIdx < k) {
        answer[ansIdx++] = -1;
    }
    
    return answer;
}