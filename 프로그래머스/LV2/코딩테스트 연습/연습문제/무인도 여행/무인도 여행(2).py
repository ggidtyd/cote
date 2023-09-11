from collections import deque

def solution(maps):
    answer = []
    R, C = len(maps), len(maps[0])
    visit = [[False] * C for _ in range(R)]
    move = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    
    for r in range(R):
        for c in range(C):
            if maps[r][c] == 'X': continue
            if visit[r][c]: continue

            s = int(maps[r][c])
            q = deque([(r, c)])
            visit[r][c] = True

            while q:
                cur = q.popleft()

                for m in move:
                    next_r, next_c = cur[0] + m[0], cur[1] + m[1]
                    if next_r < 0 or next_r >= R or next_c < 0 or next_c >= C: continue
                    if maps[next_r][next_c] == 'X': continue
                    if visit[next_r][next_c]: continue
                    visit[next_r][next_c] = True
                    s += int(maps[next_r][next_c])
                    q.append((next_r, next_c))

            answer.append(s)
    if len(answer) == 0:
        answer.append(-1)
    return sorted(answer)