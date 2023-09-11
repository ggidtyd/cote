from math import log2, floor

def check(n, l):
    if n == 0 or l == 1:
        return 1

    mid = l // 2
    left = ((1 << mid) - 1) & (n >> (mid + 1))
    right = ((1 << mid) - 1) & n

    if ((n >> mid) & 1) and check(left, mid) and check(right, mid):
        return 1
    
    return 0


def solution(numbers):
    answer = []

    for number in numbers:
        b_len = floor(log2(number)) + 1
        h = floor(log2(b_len)+1)
        total_len = 2 ** h - 1
        answer.append(check(number, total_len))        
    return answer