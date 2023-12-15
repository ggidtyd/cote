#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// str_list_len은 배열 str_list의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* strList[], size_t strListLen, const char* ex) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)calloc(101, 1);
    
    for(int i = 0; i < strListLen; i++)
        if(strstr(strList[i], ex) == NULL)
            strcat(answer, strList[i]);
    
    return answer;
}