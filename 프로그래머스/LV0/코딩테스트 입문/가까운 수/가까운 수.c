#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// array_len은 배열 array의 길이입니다.
int solution(int array[], size_t arrayLen, int n) {
    int answer = 0, diff = 101, temp;
    
    for(int i = 0; i < arrayLen; i++) {
        temp = abs(array[i] - n);
        if(temp < diff) {
            diff = temp;
            answer = array[i];
        } else if(temp == diff) {
            answer = array[i] < answer ? array[i] : answer;
        }
    }
    
    return answer;
}