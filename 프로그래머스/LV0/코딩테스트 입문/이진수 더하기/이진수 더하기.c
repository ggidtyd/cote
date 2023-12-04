#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* bin1, const char* bin2) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)calloc(12, 1);
    int s = 0;
    
    for(int i = 0; i < strlen(bin1); i++)
        if(bin1[i] == '1')
            s += (int)pow(2, (strlen(bin1) - 1) - i);
    
    for(int i = 0; i < strlen(bin2); i++)
        if(bin2[i] == '1')
            s += (int)pow(2, (strlen(bin2) - 1) - i);
    
    answer += 11;
    while(s >= 0) {
        *answer-- = s % 2 + '0';
        s /= 2;
        if(s == 0)
            break;
    }
    answer++;
    
    return answer;
}