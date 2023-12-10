#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// strArrLen 배열 strArr의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char** solution(const char* strArr[], size_t strArrLen) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char** answer = (char**)malloc(sizeof(char*) * strArrLen);
    int ansIdx = 0;

    for (int i = 0; i < strArrLen; i++)
        if (strstr(strArr[i], "ad") == NULL)
            answer[ansIdx++] = strArr[i];

    realloc(answer, sizeof(char*) * ansIdx);
    return answer;
}