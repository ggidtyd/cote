def solution(n):
    answer = ""
    while n:
        r = n % 3
        if r == 0:
            answer = "4" + answer
            n -= 1
            # n -= 2
            # n -= 3
        else:
            answer = str(r) + answer
        n //= 3
    return answer

