#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int compare(void* arg1, void* arg2) {
    return strcmp(*(char**)arg1, *(char**)arg2);
}

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char** solution(const char* myString) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char** answer = (char**)malloc(strlen(myString) * sizeof(char*));
    char* p = myString;
    
    for(int i = 0; i < strlen(myString); i++)
        answer[i] = p++;
    
    qsort(answer, strlen(myString), sizeof(char*), compare);
    
    return answer;
}