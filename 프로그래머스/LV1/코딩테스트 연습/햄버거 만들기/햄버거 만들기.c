#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// ingredient_len은 배열 ingredient의 길이입니다.
int solution(int ingredient[], size_t ingredient_len) {
    int answer = 0;
    int top = 0;
    char compare[4] = { 1,2,3,1 };
    char* stack = (char*)malloc(ingredient_len);
    
    for (int i = 0; i < ingredient_len; i++) {
        stack[top] = (char)ingredient[i];
        top++;

        if (top >= 3 && !memcmp(&stack[top - 4], compare, 4)) {
            answer++;
            top -= 4;
        }
    }
    return answer;
}