def solution(n):
    fibos = {1:1, 2:2}
    for i in range(3, n+1):
        fibos[i] = (fibos[i-2] + fibos[i-1]) % 1000000007
    return fibos[n]
