#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool check(char* q)
{
    int left = 0;
    int right = 0;
    char* p;
    
    p = strstr(q, "+") != NULL ? strstr(q, "+") : strstr(q, " -");
    left = p[0] == '+' ? atoi(q) + atoi(p + 1) : atoi(q) - atoi(p + 2);
    right = atoi(strstr(q, "=") + 1);

    return left == right ? true : false;
}

// quizLen은 배열 quiz의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char** solution(const char** quiz, size_t quizLen)
{
    int ansIdx = 0;
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char** answer = (char**)malloc(quizLen * sizeof(char*));
    
    for (int i = 0; i < quizLen; i++)
        answer[ansIdx++] = check(quiz[i]) ? "O" : "X";

    return answer;
}