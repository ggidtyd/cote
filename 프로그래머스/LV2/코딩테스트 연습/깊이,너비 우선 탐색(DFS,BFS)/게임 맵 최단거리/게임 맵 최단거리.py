from collections import deque

def get_connections(maps, cp, move, N, M):
    connections = []
    for m in move:
        next_r, next_c = cp[0] + m[0], cp[1] + m[1]
        if 0 <= next_r < N and 0 <= next_c < M:
            if maps[next_r][next_c] == 1:
                connections.append([next_r, next_c])
    return connections

def solution(maps):
    answer = -1
    N, M = len(maps), len(maps[0])
    move = [[0,1], [0,-1], [1,0], [-1,0]]
    start = [0,0]
    end = [N-1, M-1]
    maps[0][0] = 0
    q = deque([[start, 1]])

    while q:
        cur_point, level = q.popleft()

        if cur_point == end:
            answer = level
            break

        connections = get_connections(maps, cur_point, move, N, M)
        for con in connections:
            q.append([con, level+1])
            maps[con[0]][con[1]] = 0

    return answer