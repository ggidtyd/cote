from collections import deque


def solution(n, computers):
    answer = 0
    graph = {i : [] for i in range(n)}

    for i in range(len(computers)-1):
        for j in range(i+1, len(computers[0])):
            if computers[i][j]:
                graph[i].append(j)
                graph[j].append(i)

    visit = [False] * n

    for i in range(n):
        if visit[i]: continue
        answer += 1
        q = deque([i])
        visit[i] = True
        
        while q:
            cur = q.popleft()

            for adj in graph[cur]:
                if visit[adj]: continue
                visit[adj] = True
                q.append(adj)

    return answer