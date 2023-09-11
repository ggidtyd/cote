def get_o_x_cnt(board):
    x_cnt, o_cnt = 0, 0
    for r in range(3):
        for c in range(3):
            if board[r][c] == 'O':
                o_cnt += 1
            elif board[r][c] == 'X':
                x_cnt += 1
    return o_cnt, x_cnt
                

def get_matrix_vertical(board):
    board_v = []
    for c in range(3):
        temp = ""
        for r in range(3):
            temp += board[r][c]
        board_v.append(temp)
    return board_v

    
def solution(board):
    threes = []
    board_v = get_matrix_vertical(board)
    o_cnt, x_cnt = get_o_x_cnt(board)
    ooo_cnt, xxx_cnt = 0, 0

    for b, bt in zip(board, board_v):
        threes += [b, bt]
    
    d1, d2 = "", ""
    for i in range(3):
        d1 += board[i][i]
        d2 += board[i][2-i]
    threes += [d1, d2]
    
    ooo_cnt, xxx_cnt = threes.count('OOO'), threes.count('XXX')
    
    if (o_cnt - x_cnt < 0 or o_cnt - x_cnt > 1) or \
       (ooo_cnt >= 1 and xxx_cnt >= 1) or \
       (ooo_cnt == 1 and (x_cnt != (o_cnt-1))) or \
       (xxx_cnt == 1 and (o_cnt != x_cnt)):
        return 0
    return 1