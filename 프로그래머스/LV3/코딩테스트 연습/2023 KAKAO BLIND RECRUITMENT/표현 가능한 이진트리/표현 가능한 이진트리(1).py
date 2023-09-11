from math import log2, floor

def check(b):
    if len(b) == 1 or int(b) == 0:
        return 1

    idx = len(b) // 2
    left = b[:idx]
    right = b[idx+1:]

    if b[idx] == '1' and check(left) and check(right):
        return 1

    return 0


def solution(numbers):
    answer = []

    for number in numbers:
        b = bin(number)[2:]
        h = floor(log2(len(b))+1)
        total_cnt = 2 ** h - 1
        b = "0" * (total_cnt-len(b)) + b

        answer.append(check(b))        

    return answer
