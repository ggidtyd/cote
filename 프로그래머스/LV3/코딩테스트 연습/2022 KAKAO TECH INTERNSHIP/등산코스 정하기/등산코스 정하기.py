import heapq

def solution(n, paths, gates, summits):
    graph = {i:[] for i in range(1, n+1)}
    dp = {i:10000001 for i in range(1, n+1)}
    ss = set(summits)
    q = []

    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
    
    for gate in gates:
        q.append((0, gate))
        dp[gate] = 0

    while q:
        cw, cn = heapq.heappop(q)

        if cn in ss or dp[cn] < cw:
            continue

        for node, w in graph[cn]:
            nw = max(cw, w)
            if nw < dp[node]:
                dp[node] = nw
                heapq.heappush(q, (nw, node))

    result = sorted([[summit, dp[summit]] for summit in summits], key=lambda x:(x[1], x[0]))

    return result[0]