def go(numbers, idx, n, s):
    ret = 0

    if s == n:
        return 1

    if s > n or idx == len(numbers):
        return 0

    ret = go(numbers, idx+1, n, s+numbers[idx])

    return ret

def solution(n):
    ans = 0
    numbers = list(range(1, n+1))

    for i in range(n):
        ans += go(numbers, i, n, 0)
    return ans