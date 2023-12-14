#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int kCnt(n, k) {
    int cnt = 0;
    
    while(n) {
        if(n % 10 == k)
            cnt++;
        n /= 10;
    }
    
    return cnt;
}

int solution(int i, int j, int k) {
    int answer = 0;
    
    for(int n = i; n <= j; n++)
        answer += kCnt(n, k);
    
    return answer;
}