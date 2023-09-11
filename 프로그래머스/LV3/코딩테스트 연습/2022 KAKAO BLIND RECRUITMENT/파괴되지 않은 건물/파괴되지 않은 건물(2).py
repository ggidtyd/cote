def solution(board, skill):
    R, C = len(board), len(board[0])
    tboard = [[0]*(C+1) for _ in range(R+1)]

    for typ, r1, c1, r2, c2, degree in skill:
        if typ == 1: degree *= -1
        tboard[r1][c1] += degree
        tboard[r2+1][c2+1] += degree
        tboard[r2+1][c1] -= degree
        tboard[r1][c2+1] -= degree

    for c in range(1, C):
        tboard[0][c] += tboard[0][c-1]
    for r in range(1, R):
        tboard[r][0] += tboard[r-1][0]
    for r in range(1, R):
        for c in range(1, C):
            tboard[r][c] += tboard[r][c-1] + tboard[r-1][c] - tboard[r-1][c-1]

    ans = 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c]+tboard[r][c] > 0: ans += 1
    return ans