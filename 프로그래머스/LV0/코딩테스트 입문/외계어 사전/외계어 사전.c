#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// spell_len은 배열 spell의 길이입니다.
// dic_len은 배열 dic의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* spell[], size_t spellLen, const char* dic[], size_t dicLen) {
    int answer = 2;
    bool alphabets[26] = {false, };
    bool used[26] = {false, };
    bool flag;
    
    for(int i = 0; i < spellLen; i++)
        alphabets[spell[i][0] - 'a'] = true;
    
    for(int i = 0; i < dicLen; i++) {
        flag = true;

        for(int j = 0; j < strlen(dic[i]); j++) {
            if(strlen(dic[i]) != spellLen || used[dic[i][j] - 'a'] || !alphabets[dic[i][j] - 'a']) {
                flag = false;
                break;
            }
            used[dic[i][j] - 'a'] = true;
        }
        
        if(flag) {
            answer = 1;
            break;
        }
        
        for(int j = 0; j < strlen(dic[i]); j++)
            used[dic[i][j] - 'a'] = false;
    }
    
    return answer;
}