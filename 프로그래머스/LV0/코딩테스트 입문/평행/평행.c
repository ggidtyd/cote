#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// dots_rows는 2차원 배열 dots의 행 길이, dots_cols는 2차원 배열 dots의 열 길이입니다.
int solution(int** dots, size_t dotsRows, size_t dotsCols) {
    int others[2] = {0, };
    int oIdx;
    double a1, a2;
    
    for(int i = 0; i < dotsRows; i++) {
        for(int j = i + 1; j < dotsRows; j++) {
            oIdx = 0;
            a1 = (double)(dots[i][1] - dots[j][1]) / (double)(dots[i][0] - dots[j][0]);
            
            for(int k = 0; k < 4; k++)
                if(k != i && k != j)
                    others[oIdx++] = k;
            
            a2 = (double)(dots[others[0]][1] - dots[others[1]][1]) /
                (double)(dots[others[0]][0] - dots[others[1]][0]);
            
            if(a1 == a2)
                return 1;
        }
    }
    
    return 0;
}