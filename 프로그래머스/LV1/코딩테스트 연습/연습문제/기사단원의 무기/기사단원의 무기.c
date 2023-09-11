#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>
int get_number_of_divisors(int n) {
    int ret = 0;

    for(int i = 1; i <= (int)pow(n, 0.5); i++) {
        if(i*i == n)ret++;
        else if(n % i == 0)ret += 2;
    }
    return ret;
}

int solution(int number, int limit, int power) {
    int answer = 0;
    int p;
    for(int i = 1; i <= number; i++) {
        p = get_number_of_divisors(i);
        answer += p > limit ? power : p; 
    }
        
    return answer;
}