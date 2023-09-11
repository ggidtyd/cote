#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

int count_composite_number(n) {
    int ret = 0;
    bool* sieve = malloc(n + 1);
    memset(sieve, true, n + 1);

    int m = (int)pow(n, 0.5);

    for (int i = 2; i <= m; i++) {
        if (sieve[i] == true) {
            for (int j = 2 * i; j <= n; j += i) {
                sieve[j] = false;
            }
        }
    }

    for (int i = 2; i <= n; i++) {
        if (!sieve[i])ret++;
    }

    return ret;
}

int solution(int n) {
    return count_composite_number(n);
}