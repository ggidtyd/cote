from collections import deque


def solution(n, roads, sources, destination):
    distances = [-1 for _ in range(n+1)]
    graph = {i : [] for i in range(1, n+1)}

    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])

    q = deque([[destination, 0]])
    distances[destination] = 0

    while q:
        cur, d = q.popleft()

        for n in graph[cur]:
            if distances[n] == -1:
                distances[n] = d + 1
                q.append([n, d+1])

    return [distances[s] for s in sources]