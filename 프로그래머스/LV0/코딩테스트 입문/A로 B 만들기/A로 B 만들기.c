#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* before, const char* after) {
    int alphaCntBef[26] = {0, };
    int alphaCntAft[26] = {0, };
    
    for(int i = 0; i < strlen(before); i++) {
        alphaCntBef[before[i] - 'a']++;
        alphaCntAft[after[i] - 'a']++;
    }
    
    for(int i = 0; i < 26; i++)
        if(alphaCntBef[i] != alphaCntAft[i])
            return 0;
    
    return 1;
}