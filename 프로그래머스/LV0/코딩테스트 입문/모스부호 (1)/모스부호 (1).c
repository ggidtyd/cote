#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* letter) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* letterCpy = (char*)calloc(strlen(letter) + 2, 1);
    strcpy(letterCpy, letter);
    letterCpy[strlen(letter)] = ' ';
    char receivedMorses[1000][5] = { 0, };
    char answer[1000] = { 0, };
    int ansIdx = 0, morseIdx = 0;

    char morse[26][5] = {
        ".-","-...","-.-.","-..",".","..-.","--.","....","..",
        ".---","-.-",".-..","--","-.","---",".--.","--.-",
        ".-.","...","-","..-","...-",".--","-..-","-.--","--.." };

    char* front = letterCpy;
    char* p = strstr(front, " ");

    while (p != NULL) {
        strncpy(receivedMorses[morseIdx], front, p - front);
        
        for (int i = 0; i < 26; i++) {
            if (strcmp(receivedMorses[morseIdx], morse[i]) == 0) {
                answer[ansIdx++] = i + 'a';
                break;
            }
        }
        
        morseIdx++;
        front = p + 1;
        p = strstr(front, " ");
    }

    return answer;
}