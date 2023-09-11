def go(value, mat, left_top, right_bottom, r, c, rcs, R, C):
    mat[r][c] = abs(value - 1)
    
    for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        next_r, next_c = r + dr, c + dc
        if next_r < 0 or next_r >= R or next_c < 0 or next_c >= C: continue
        if mat[next_r][next_c] != value: continue
        left_top[0], left_top[1] = min(left_top[0], next_r), min(left_top[1], next_c)
        right_bottom[0], right_bottom[1] = max(right_bottom[0], next_r), max(right_bottom[1], next_c)
        rcs.append((next_r, next_c))
        go(value, mat, left_top, right_bottom, next_r, next_c, rcs, R, C)


def rotated(a):
    n = len(a)
    m = len(a[0])
    result = [[0]* n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result


def mat_to_str(mat):
    mat_str = ""
    for row in mat:
        mat_str += "".join(map(str, row)) + 'a'
    return mat_str


def get_shape(r, c, value, table, R, C):
    rcs = [(r, c)]
    left_top, right_bottom = [r, c], [r, c]
    go(value, table, left_top, right_bottom, r, c, rcs, R, C)
    w = right_bottom[1] - left_top[1] + 1
    h = right_bottom[0] - left_top[0] + 1 
    shape = [[0] * w for _ in range(h)]
    for x, y in rcs:
        shape[x-left_top[0]][y-left_top[1]] = 1

    if value == 0:
        return shape
    elif value == 1:
        shapes = [shape]
        for _ in range(3):
            shapes.append(rotated(shapes[-1]))
        return shapes


def get_table_shapes(tr, tc, table):
    table_shape_dict = dict()
    table_shape_dict_key = 0

    for r in range(tr):
        for c in range(tc):
            if table[r][c] == 1:
                shapes = get_shape(r, c, 1, table, tr, tc)
                table_shape_dict[table_shape_dict_key] = set()
                for shp in shapes:
                    shp_str = mat_to_str(shp)
                    table_shape_dict[table_shape_dict_key].add(shp_str)
                table_shape_dict_key += 1
    return table_shape_dict


def solution(game_board, table):
    ans = 0
    gb_r, gb_c = len(game_board), len(game_board[0])
    table_shapes_dict = get_table_shapes(len(table), len(table[0]), table)
    used = [False] * len(table_shapes_dict)
    for r in range(gb_r):
        for c in range(gb_c):
            if game_board[r][c] == 0:
                shape = get_shape(r, c, 0, game_board, gb_r, gb_c)
                shape_str = mat_to_str(shape)
                for k, v in table_shapes_dict.items():
                    if used[k]: continue
                    if shape_str in v:
                        ans += shape_str.count('1')
                        used[k] = True
                        break
    return ans