import sys
sys.setrecursionlimit(100000000)

def go(maps, r, c, move, visit, R, C):
    s = 0
    visit[r][c] = True
    s += int(maps[r][c])
    for m in move:
        next_r, next_c = r + m[0], c + m[1]
        if next_r < 0 or next_r >= R or next_c < 0 or next_c >= C: continue
        if maps[next_r][next_c] == 'X': continue
        if visit[next_r][next_c]: continue
        s += go(maps, next_r, next_c, move, visit, R, C)
    return s


def solution(maps):
    answer = []
    R, C = len(maps), len(maps[0])
    visit = [[False] * C for _ in range(R)]
    move = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    for r in range(R):
        for c in range(C):
            if maps[r][c] == 'X': continue
            if visit[r][c]: continue
            answer.append(go(maps, r, c, move, visit, R, C))

    if len(answer) == 0:
        answer.append(-1)
    return sorted(answer)