def get_max_excluding_current_col_in_up_row(cur_col, up_row):
    return max(up_row[:cur_col] + up_row[cur_col+1:])
    
def solution(land):
    answer = 0
    row = len(land)
    
    for r in range(1, row):
        for c in range(4):
            land[r][c] += get_max_excluding_current_col_in_up_row(c, land[r-1])
    return max(land[row-1])

