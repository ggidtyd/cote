def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        if n**(1/2) % 1 == 0:
            answer -= n
        else:
            answer += n
    return answer