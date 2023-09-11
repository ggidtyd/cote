from collections import deque


def get_r_g(W, H, board):
    R, G = [], []
    for i in range(H):
        if R != [] and G != []:
            break
        for j in range(W):
            if board[i][j] == 'R':
                R = [i, j]
            elif board[i][j] == 'G':
                G = [i, j]
    return R, G


def get_next(cur, d, board, W, H):
    if d == "상":
        for i in range(cur[0], -1, -1):
            if board[i][cur[1]] == 'D':
                return [i+1, cur[1]]                
        else:
            return [0, cur[1]]
    elif d == "하":
        for i in range(cur[0], H):
            if board[i][cur[1]] == 'D':
                return [i-1, cur[1]]
        else:
            return [H-1, cur[1]]
    elif d == "좌":
        for i in range(cur[1], -1, -1):
            if board[cur[0]][i] == 'D':
                return [cur[0], i+1]
        else:
            return [cur[0], 0]
    elif d == "우":
        for i in range(cur[1], W):
            if board[cur[0]][i] == 'D':
                return [cur[0], i-1]
        else:
            return [cur[0], W-1]


def solution(board):
    W, H = len(board[0]), len(board)
    dirs = ["상", "하", "좌", "우"]
    visit = [[False] * W for _ in range(H)]
    R, G = get_r_g(W, H, board)

    q = deque([[R, 0]])
    visit[R[0]][R[1]] = True

    while q:
        cur, cnt = q.popleft()

        if cur == G:
            return cnt
        
        for d in dirs:
            next_point = get_next(cur, d, board, W, H)
            if visit[next_point[0]][next_point[1]]:
                continue
            visit[next_point[0]][next_point[1]] = True
            q.append([next_point, cnt+1])

    return -1