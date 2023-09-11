def solution(board):
    max = 0
    R, C = len(board), len(board[0])
    
    if R <= 1 or C <= 1:
        return 1

    for r in range(1,R):
        for c in range(1,C):
            if board[r][c] == 1:
                board[r][c] = min(board[r-1][c], board[r][c-1], board[r-1][c-1]) + 1

                if board[r][c] > max :
                    max = board[r][c]
    return max**2