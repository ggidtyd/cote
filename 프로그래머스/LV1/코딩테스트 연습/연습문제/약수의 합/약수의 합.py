def cal(mid_v, n):
    ret = 0
    for i in range(1, mid_v):
        if n % i == 0:
            ret += i
            ret += n // i    
    return ret


def solution(n):
    answer = 0
    mid_v = int(n**0.5)
    if n**0.5 % 1 == 0:
        answer = cal(mid_v, n)
        answer += mid_v
    else:
        answer = cal(mid_v+1, n)
    return answer