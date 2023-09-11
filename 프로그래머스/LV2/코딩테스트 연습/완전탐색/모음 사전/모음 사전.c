#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>
int previous_count(char n) {
    switch (n)
    {
    case 'A':
        return 0;
    case 'E':
        return 1;
    case 'I':
        return 2;
    case 'O':
        return 3;
    case 'U':
        return 4;    
    }
}

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* word) {
    int answer = 0;
    int vowel_pos = 0;
    for(int i = 0; i < strlen(word); i++) {
        answer += ((5 * (pow(5, 4 - i) - 1) / 4) + 1) * previous_count(word[i]) + 1;
    }
    return answer;
}