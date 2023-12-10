#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int a, int b, int c, int d) {
    int answer = 0;
    int diceCnt[7] = {0, };
    int p = 0, q = 0, r = 0;
    int mul = 1, minv = 7;
    
    diceCnt[a]++;
    diceCnt[b]++;
    diceCnt[c]++;
    diceCnt[d]++;
    
    for(int i = 1; i < 7; i++) {
        if(diceCnt[i] == 0)
            continue;
        mul *= diceCnt[i];
        if(diceCnt[i] == 4) {
            p = i;
            break;
        } else if(diceCnt[i] == 3) {
            p = i;
        } else if(diceCnt[i] == 2) {
            if(p == 0)
                p = i;
            else
                q = i;
        } else if(diceCnt[i] == 1) {
            if(q == 0)
                q = i;
            else
                r = i;
            if(i < minv)
                minv = i;
        }
    }
    
    switch(mul) {
        case 4:
            if(q == 0)
                answer = 1111 * p;
            else
                answer = (p + q) * abs(p - q);
            break;
        case 3:
            answer = (10 * p + q) * (10 * p + q);
            break;
        case 2:
            answer = q * r;
            break;
        case 1:
            answer = minv;
            break;
    }
    
    return answer;
}