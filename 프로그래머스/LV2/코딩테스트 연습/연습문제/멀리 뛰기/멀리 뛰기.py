def solution(n):
    if n <= 3:
        return n
    a,b = 2,3
    for i in range(4, n+1):
        answer = (a+b)%1234567
        a = b
        b = answer
    return answer
