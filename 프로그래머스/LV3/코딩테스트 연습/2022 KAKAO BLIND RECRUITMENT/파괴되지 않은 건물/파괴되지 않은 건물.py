from numpy import array


def solution(board, skills):
    R, C = len(board), len(board[0])
    board = array(board)
    arr = array([[0] * C for _ in range(R)])

    for skill in skills:
        type, r1, c1, r2, c2, degree = skill
        if type == 1: degree *= -1
        arr[r1][c1:c2+1] += degree
        if r2+1 >= R: continue
        arr[r2+1][c1:c2+1] -= degree

    for i in range(R-1):
        arr[i+1] += arr[i]

    board += arr
    return len(board[board > 0])