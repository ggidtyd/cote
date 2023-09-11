def solution(n):
    fibos = {0:0, 1:1}
    for i in range(2, n+1):
        fibos[i] = fibos[i-2] + fibos[i-1]
    return fibos[n] % 1234567