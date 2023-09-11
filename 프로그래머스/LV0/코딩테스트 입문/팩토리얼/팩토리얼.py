def solution(n):
    mul = 1
    i = 1
    while True:
        mul *= i
        if mul > n:
            break
        i += 1
    return i - 1
