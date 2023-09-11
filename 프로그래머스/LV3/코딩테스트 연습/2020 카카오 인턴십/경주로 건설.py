from collections import deque

def solution(board):
    N = len(board)
    loc_cost = [[[25 * 25 * 500 for _ in range(4)] for _ in range(N)] for _ in range(N)]
    ds = [[1,0], [0,1], [-1,0], [0,-1]]
    q = deque([[0, 0, 0, 0], [0, 0, 1, 0]])

    while q:
        r, c, pdi, cost = q.popleft()

        for di, d in enumerate(ds):
            next_r, next_c = r + d[0], c + d[1]
            if next_r < 0 or next_r >= N or next_c < 0 or next_c >= N: continue
            if board[next_r][next_c] == 1: continue

            new_cost = cost + 100 if di == pdi else cost + 600

            if new_cost < loc_cost[next_r][next_c][di]:
                loc_cost[next_r][next_c][di] = new_cost
                q.append([next_r, next_c, di, new_cost])

    return min(loc_cost[N-1][N-1])