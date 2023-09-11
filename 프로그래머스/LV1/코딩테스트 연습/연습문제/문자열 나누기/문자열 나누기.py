def solution(s):
    answer = 0
    x, x_cnt = 0, 0

    for c in s:
        if x == 0:
            x = c
            x_cnt = 1
            continue   

        x_cnt += 1 if x == c else -1
        
        if x_cnt == 0:
            answer += 1
            x = 0

    if x_cnt != 0:
        answer += 1
    return answer