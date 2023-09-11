#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int gcd(int a, int b) {
	return b ? gcd(b, a%b) : a;
}

int solution(int n) {
    return n / gcd(n, 6);
}