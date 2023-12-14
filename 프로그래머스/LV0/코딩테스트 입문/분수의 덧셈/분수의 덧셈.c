#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int gcd(int a, int b) {
	return b ? gcd(b, a % b) : a;
}

int* solution(int numer1, int denom1, int numer2, int denom2) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(sizeof(int) * 2);
    
    int d = denom1 * denom2;
    int n = numer1 * denom2 + numer2 * denom1;
    int g = gcd(n, d);
    
    answer[0] = n / g;
    answer[1] = d / g;
    
    return answer;
}