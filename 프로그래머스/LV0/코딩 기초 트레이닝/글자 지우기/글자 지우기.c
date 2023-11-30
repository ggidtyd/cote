#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// indicesLen은 배열 indices의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* myString, int indices[], size_t indicesLen) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)calloc(strlen(myString) + 1, 1);
    bool skip[101] = {false, }; 
    int ansIdx = 0;
    
    for(int i = 0; i < indicesLen; i++)
        skip[indices[i]] = true;
    
    for(int i = 0; i < strlen(myString); i++) {
        if(skip[i])
            continue;
        answer[ansIdx++] = myString[i];
    }
    
    return answer;
}