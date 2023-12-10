#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// queries_rows는 2차원 배열 queries의 행 길이, queries_cols는 2차원 배열 queries의 열 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* myString, int** queries, size_t queriesRows, size_t queriesCols) {
    int s, e, ansIdx;
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)malloc(strlen(myString) + 1);
    strcpy(answer, myString);
    
    for(int r = 0; r < queriesRows; r++) {
        s = queries[r][0], e = queries[r][1];
        char* temp = (char*)malloc(e - (s-1));
        memcpy(temp, answer + s, sizeof(char) * (e - (s-1)));
        ansIdx = s;
        for(int i = e - s; i >= 0; i--)
            answer[ansIdx++] = temp[i];
    }
    return answer;
}