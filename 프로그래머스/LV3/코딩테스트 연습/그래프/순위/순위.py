def go(wl, cur, graph, dp, path):  
    if len(dp[cur][wl]) != 0:
        path |= dp[cur][wl]
        return
    
    for n in graph[cur][wl]:
        if n in path: continue
        path.add(n)
        go(wl, n, graph, dp, path)


def solution(n, results):
    answer = 0
    graph = {i:[[], []] for i in range(1, n+1)}
    dp = [[set(), set()] for _ in range(n+1)]

    for w, l in results:
        graph[w][1].append(l)
        graph[l][0].append(w)

    for i in range(1, n+1):
        win_path, lose_path = set(), set()
        go(1, i, graph, dp, win_path)
        go(0, i, graph, dp, lose_path)
        dp[i][1] = win_path
        dp[i][0] = lose_path
        
        if len(dp[i][0]) + len(dp[i][1]) == n - 1:
            answer += 1
    return answer