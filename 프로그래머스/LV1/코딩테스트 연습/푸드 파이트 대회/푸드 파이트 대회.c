#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

struct food_numbers_and_len {
    char* fns;
    int len;
}typedef FNAL;

FNAL get_fnal(int food[], int food_len) {
    FNAL fnal;
    int len = 0;
    int fns_idx = 0;
    char* fns = (char*)malloc(food_len * 500);

    for (int i = 0; i < food_len; i++) {
        len += food[i] / 2;
        memset(&fns[fns_idx], i + '0', food[i] / 2);
        fns_idx += food[i] / 2;
    }
    fns[len] = '\0';
    fnal.fns = fns;
    fnal.len = len;
    return fnal;
}

// food_len은 배열 food의 길이입니다.
char* solution(int food[], size_t food_len)
{
    int ans_idx = 0;
    FNAL fnal = get_fnal(food, food_len);
    char* answer = (char*)malloc(fnal.len * 2 + 1);
    
    strcpy(answer, fnal.fns);
    answer[fnal.len] = '0';
    ans_idx = fnal.len + 1;
    
    for(int i = fnal.len-1; i >= 0; i--)
        answer[ans_idx++] = fnal.fns[i];
    answer[ans_idx] = '\0';
    
    return answer;
}