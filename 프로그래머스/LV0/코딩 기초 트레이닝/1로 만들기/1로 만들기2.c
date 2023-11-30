#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// num_list_len은 배열 num_list의 길이입니다.
int solution(int numList[], size_t numListLen) {
    int answer = 0;
    int dp[31] = {0, };
    dp[2] = 1;

    for(int i = 3; i < 31; i++)
        dp[i] = i % 2 == 0 ? dp[i / 2]+1 : dp[i - 1];

    for(int i = 0; i < numListLen; i++)
        answer += dp[numList[i]];

    return answer;
}