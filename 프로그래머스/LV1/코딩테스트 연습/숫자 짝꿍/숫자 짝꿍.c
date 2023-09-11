#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* x, const char* y) {
    char* answer;
    char* temp;
    int x_dict[10] = { 0, };
    int y_dict[10] = { 0, };
    int xy_dict[10] = { 0, };
    int intersection_len = 0;
    int ans_size = 0;

    for (int i = 0; i < strlen(x); i++)x_dict[x[i] - '0']++;
    for (int i = 0; i < strlen(y); i++)y_dict[y[i] - '0']++;
    

    for (int i = 0; i < 10; i++) {
        xy_dict[i] = x_dict[i] < y_dict[i] ? x_dict[i] : y_dict[i];
        if (xy_dict[i] != 0)intersection_len++;
        ans_size += xy_dict[i];
    }

    if (!intersection_len)return "-1";
    if (intersection_len == 1 && xy_dict[0])return "0";

    answer = (char*)malloc(ans_size + 1);
    memset(answer, 0, ans_size + 1);
    for (int i = 9; i >= 0; i--) {
        temp = (char*)malloc(xy_dict[i] + 1);
        for (int j = 0; j < xy_dict[i]; j++) {
            temp[j] = i + '0';
        }
        temp[xy_dict[i]] = '\0';
        strcat(answer, temp);
    }
    return answer;
}