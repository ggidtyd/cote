def solution(n):
    answer = 0
    n_cnt = bin(n).count('1')
    while True:
        if bin(n+1).count('1') == n_cnt:
            answer = n+1
            break
        n += 1
    return answer