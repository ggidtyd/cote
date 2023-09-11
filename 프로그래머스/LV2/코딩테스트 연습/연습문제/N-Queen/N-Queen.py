in_attack_range_col = []
in_attack_range_d1 = []
in_attack_range_d2 = []

def go(row, n):
    global in_attack_range_col, in_attack_range_d1, in_attack_range_d2
    answer = 0

    if row == n:
        return 1

    for i in range(n):
        d1 = row + i
        d2 = n + row - i
        if in_attack_range_col[i] == False and in_attack_range_d1[d1] == False and in_attack_range_d2[d2] == False:
            in_attack_range_col[i] = True
            in_attack_range_d1[d1] = True
            in_attack_range_d2[d2] = True
            answer += go(row+1, n)
            in_attack_range_col[i] = False
            in_attack_range_d1[d1] = False
            in_attack_range_d2[d2] = False
    return answer

def solution(n):
    global in_attack_range_col, in_attack_range_d1, in_attack_range_d2
    in_attack_range_col = [False] * n
    in_attack_range_d1 = [False] * 2 * n
    in_attack_range_d2 = [False] * 2 * n
    return go(0, n)