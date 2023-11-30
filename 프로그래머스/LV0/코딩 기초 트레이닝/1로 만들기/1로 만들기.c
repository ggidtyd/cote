#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// num_list_len은 배열 num_list의 길이입니다.
int solution(int numList[], size_t numListLen) {
    int answer = 0;
    
    for(int i = 0; i < numListLen; i++) {
        int cnt = 0;
        while(numList[i] != 1) {
            if(numList[i] % 2 == 0)
                numList[i] /= 2;
            else 
                numList[i] = (numList[i] - 1) / 2;
            cnt++;
        }
        answer += cnt;
    }
    return answer;
}