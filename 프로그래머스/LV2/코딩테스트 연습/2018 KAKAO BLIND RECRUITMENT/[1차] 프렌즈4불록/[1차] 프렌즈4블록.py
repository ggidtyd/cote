def same2x2(r,c,board):
    if board[r][c] == 0:
        return False
    if board[r][c] == board[r+1][c] == board[r][c+1] == board[r+1][c+1]:
        return True
    return False

def find_core_points(m,n,board):
    core_points = []
    cur_core_point_num = 0
    for r in range(m-1):
        for c in range(n-1):
            if same2x2(r,c,board):
                core_points.append((r,c))
                cur_core_point_num += 1
    return core_points, cur_core_point_num

def down(r,c,board):
    for rr in range(r):
        board[r-rr][c] = board[r-rr-1][c]
        board[r-rr-1][c] = 0

def count_and_down(m,n,board):
    cnt = 0
    for r in range(m):
        for c in range(n):
            if board[r][c] == -1:
                cnt += 1
                board[r][c] = 0
                down(r,c,board)
    return cnt

def set2x2m1(cps, board):
    for cp in cps:
        board[cp[0]][cp[1]] = -1
        board[cp[0]+1][cp[1]] = -1
        board[cp[0]][cp[1]+1] = -1
        board[cp[0]+1][cp[1]+1] = -1

def solution(m, n, board):
    answer = 0
    core_points = []
    cur_core_point_num = 0

    for i in range(len(board)):
        board[i] = list(board[i])
    while True:
        core_points, cur_core_point_num = find_core_points(m,n,board)
        if cur_core_point_num == 0:
            break
        set2x2m1(core_points,board)
        answer += count_and_down(m,n,board)
        cur_core_point_num = 0
        core_points = []
    return answer