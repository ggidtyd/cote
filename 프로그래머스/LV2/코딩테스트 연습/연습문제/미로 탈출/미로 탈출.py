from collections import deque


def bfs(maps, start, end, R, C):
    move = [[1,0], [-1,0], [0,1], [0,-1]]
    visited = [[False] * C for _ in range(R)]
    visited[start[0]][start[1]] = True
    q = deque([[start, 0]])
    
    while q:
        cur, time = q.popleft()
        if cur == end:
            return time

        for m in move:
            next_r, next_c = cur[0] + m[0], cur[1] + m[1]
            if next_r < 0 or next_r >= R or next_c < 0 or next_c >= C: continue
            if maps[next_r][next_c] == 'X': continue
            if visited[next_r][next_c]: continue
            visited[next_r][next_c] = True
            q.append([[next_r, next_c], time+1])
            
    return -1


def get_s_e_l(maps, R, C):
    s, e, l = None, None, None
    for r in range(R):
        for c in range(C):
            if s != None and e != None and l != None:
                return s, e, l
            
            if maps[r][c] == 'S':
                s = [r, c]
            elif maps[r][c] == 'E':
                e = [r, c]
            elif maps[r][c] == 'L':
                l = [r, c]
    return s, e, l
                
    
def solution(maps):
    R, C = len(maps), len(maps[0])
    s, e, l = get_s_e_l(maps, R, C)
    
    to_l = bfs(maps, s, l, R, C)
    if to_l == -1: return -1
    to_e = bfs(maps, l, e, R, C)
    if to_e == -1: return -1

    return to_l + to_e