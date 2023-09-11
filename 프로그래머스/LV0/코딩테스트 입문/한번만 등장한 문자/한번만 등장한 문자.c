#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int count(char* str, char c) {
    int cnt = 0;
    char* p = strchr(str, c);
    while (p != NULL) {
        cnt++;
        p = strchr(p + 1, c);
    }
    return cnt;
}

int compare(const char* p1, const char* p2) {
    return *p1 - *p2; // 오름차순
}

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* s) {
    int cnt = 0;
    int ans_idx = 0;
    int len = strlen(s);
    char* answer = (char*)malloc(len);
    char* str = (char*)malloc(len);

    strcpy(str, s);
    char* p;

    qsort(str, len, 1, compare);

    for (int i = 0; i < len; i++) {        
        if (count(str, str[i]) == 1)
            answer[ans_idx++] = str[i];
    }
    answer[ans_idx] = '\0';
    return answer;
}