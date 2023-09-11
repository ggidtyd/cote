#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool continous_check(char* b, char* cs) {
    char temp[61] = { 0, };
    strcat(temp, cs);
    strcat(temp, cs);
    if (strstr(b, temp) != NULL) return true;
    return false;
}

bool consist_of_can_speak(char* b) {
    for (int i = 0; i < strlen(b); i++) {
        if (b[i] != '-')return false;
    }
    return true;
}

// babbling_len은 배열 babbling의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* babbling[], size_t babbling_len) {
    char** bb = (char**)malloc(sizeof(char*) * babbling_len);
    for (int i = 0; i < babbling_len; i++) {
        bb[i] = (char*)malloc(31);
        strcpy(bb[i], babbling[i]);
    }

    char* p;
    char can_speak[4][4] = { "aya", "ye", "woo", "ma" };
    bool continuous_pronunciation = true;
    int answer = 0;

    for (int i = 0; i < babbling_len; i++) {
        for (int j = 0; j < 4; j++) {
            continuous_pronunciation = continous_check(bb[i], can_speak[j]) ? true : false;
            if (continuous_pronunciation)break;

            p = strstr(bb[i], can_speak[j]);
            while (p != NULL) {
                memset(p, '-', strlen(can_speak[j]));
                p = strstr(bb[i], can_speak[j]);
            }

        }
        if (!continuous_pronunciation && consist_of_can_speak(bb[i])) answer++;
    }
    return answer;
}