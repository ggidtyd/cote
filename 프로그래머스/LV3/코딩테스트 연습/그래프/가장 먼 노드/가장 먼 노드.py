from collections import deque

def solution(n, edge):
    graph = {i:[] for i in range(1, n+1)}
    for i, j in edge:
        graph[i].append(j)
        graph[j].append(i)
    dp = [20001] * (n+1)
    dp[0] = -1
    dp[1] = 0
    q = deque([(1, 0)])

    while q:
        cn, d = q.popleft()

        for nn in graph[cn]:
            if dp[nn] > d+1:
                dp[nn] = min(dp[nn], d+1)
                q.append((nn, dp[nn]))

    return dp.count(max(dp))