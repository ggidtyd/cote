#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* check(char* q) {
        int xyz[3] = { 0, };
        int xyzIdx = 0;
        char op = 0;
        char* spacePointer = 0;

        for (int i = 0; i < 3; i++) {
            xyz[xyzIdx++] = atoi(q);
            spacePointer = strstr(q, " ");
            if (i == 0)
                op = *(spacePointer + 1);
            q = spacePointer + 3;
        }

        if (op == '-')
            return xyz[0] - xyz[1] == xyz[2] ? "O" : "X";
        else
            return xyz[0] + xyz[1] == xyz[2] ? "O" : "X";
}

// quizLen은 배열 quiz의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char** solution(const char* quiz[], size_t quizLen) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char** answer = (char**)malloc(quizLen * sizeof(char*));
    int ansIdx = 0;

    for (int i = 0; i < quizLen; i++)
        answer[ansIdx++] = check(quiz[i]);

    return answer;
}