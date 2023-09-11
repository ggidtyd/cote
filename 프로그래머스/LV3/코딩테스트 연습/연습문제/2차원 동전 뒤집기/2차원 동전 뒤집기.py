from numpy import array_equal, ones, int8
from collections import Counter


def flip_row(beginning, flips):
    for i, flip in enumerate(flips):
        if flip: beginning[i] = ~beginning[i]
    return Counter(flips)[True]


def flip_col(beginning, flips):
    for i, flip in enumerate(flips):
        if flip: beginning[:, i] = ~beginning[:, i]
    return Counter(flips)[True]


def row_first(beginning, target, flips_r):
    cnt = flip_row(beginning, flips_r)
    cnt += flip_col(beginning, beginning[0] != target[0])
    return cnt if array_equal(beginning, target) else -1


def col_first(beginning, target, flips_c):
    cnt = flip_col(beginning, flips_c)
    cnt += flip_row(beginning, beginning[:, 0] != target[:, 0])
    return cnt if array_equal(beginning, target) else -1


def solution(beginning, target):
    R, C= len(beginning), len(beginning[0])
    cmp = ones(shape=(R, C), dtype=int8)
    beginning = beginning == cmp
    target = target == cmp

    answer = 101
    cur = row_first(beginning.copy(), target.copy(), beginning[:, 0] == target[:, 0])
    if cur == -1: return cur
    else: answer = min(answer, cur)

    cur = row_first(beginning.copy(), target.copy(), beginning[:, 0] != target[:, 0])
    if cur == -1: return cur
    else: answer = min(answer, cur)

    cur = col_first(beginning.copy(), target.copy(), beginning[0] == target[0])
    if cur == -1: return cur
    else: answer = min(answer, cur)

    cur = col_first(beginning.copy(), target.copy(), beginning[0] != target[0])
    if cur == -1: return cur
    else: answer = min(answer, cur)

    return answer