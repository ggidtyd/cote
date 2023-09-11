from math import gcd

def solution(arr):
    answer = 1
    for v in arr:
        answer = v * answer // gcd(v,answer)
    return answer