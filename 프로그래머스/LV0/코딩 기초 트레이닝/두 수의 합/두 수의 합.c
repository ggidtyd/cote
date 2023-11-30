#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* a, const char* b) {
    int shortLen = 0, longLen = 0;
    char* ap = a + (strlen(a) - 1);
    char* bp = b + (strlen(b) - 1);
    char* remainp;

    if (strlen(a) > strlen(b)) {
        shortLen = strlen(b);
        longLen = strlen(a);
        remainp = a + (strlen(a) - strlen(b) - 1);
    }
    else {
        longLen = strlen(b);
        shortLen = strlen(a);
        remainp = b + (strlen(b) - strlen(a) - 1);
    }

    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)calloc(longLen + 2, 1);
    int ansIdx = longLen;
    int an, bn, rn, s, n, carry = 0;
    int remain = longLen - shortLen;

    while (shortLen--) {
        an = *ap-- - '0';
        bn = *bp-- - '0';
        s = an + bn + carry;
        carry = s / 10;
        n = s % 10;

        answer[ansIdx--] = n + '0';
    }

    while (remain--) {
        rn = *remainp-- - '0';
        s = rn + carry;
        carry = s / 10;
        n = s % 10;

        answer[ansIdx--] = n + '0';
    }

    if (carry == 1)
        answer[0] = '1';
    else
        answer++;

    return answer;
}