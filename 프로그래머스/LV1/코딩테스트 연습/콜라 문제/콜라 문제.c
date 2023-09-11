#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int a, int b, int n) {
    return ((n - a) / (a - b) + 1) * b;
}