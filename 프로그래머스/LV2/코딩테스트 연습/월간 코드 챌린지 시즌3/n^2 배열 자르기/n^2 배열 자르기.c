#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int n, long long left, long long right) {
    int* answer = (int*)malloc(sizeof(long long) * (right - left + 1));
    for(long long i = left; i <= right; i++)answer[i-left] = i / n > i % n ? i / n + 1 : i % n + 1;
    return answer;
}