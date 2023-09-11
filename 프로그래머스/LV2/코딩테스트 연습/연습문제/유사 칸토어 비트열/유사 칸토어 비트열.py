from math import log

def get_left_cnt(x):
    if x <= 5: return '11011'[:x].count('1')

    before_level = int(log(x, 5))
    if 5 ** before_level == x: before_level -= 1

    q = x // (5 ** before_level)
    r = x % (5 ** before_level)

    answer = q * (4 ** before_level)

    if q >= 3: answer -= (4 ** before_level)

    if q == 2: return answer
    else: return answer + get_left_cnt(r)

def solution(n, l, r):
    return get_left_cnt(r) - get_left_cnt(l-1)