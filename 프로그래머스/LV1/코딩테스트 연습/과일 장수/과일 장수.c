#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int compare(int* v1, int* v2) {
    return *v1 - *v2;
}

// score_len은 배열 score의 길이입니다.
int solution(int k, int m, int score[], size_t score_len) {
    qsort(score, score_len, sizeof(int), compare);
    int answer = 0;

    for(int i = score_len % m; i < score_len; i+=m) {
        answer += score[i];
    }    
    return answer*m;
}