def solution(rows, columns, queries):
    answer = []
    origin_map = []
    
    for _ in range(rows+1):
        origin_map.append([0] * (columns+1))
    
    for r in range(1, rows+1):
        for c in range(1, columns+1):
            origin_map[r][c] = ((r-1) * columns + c)

    for query in queries:
        x1, y1, x2, y2 = query
        temp_map = []
        moved_values = []

        for row in origin_map:
            temp_map.append(row.copy())
        
        for c in range(y1, y2):
            origin_map[x1][c+1] = temp_map[x1][c]
            origin_map[x2][c] = temp_map[x2][c+1]
            moved_values.append(temp_map[x1][c])
            moved_values.append(temp_map[x2][c+1])

        for r in range(x1, x2):
            origin_map[r+1][y2] = temp_map[r][y2]
            origin_map[r][y1] = temp_map[r+1][y1]
            moved_values.append(temp_map[r][y2])
            moved_values.append(temp_map[r+1][y1])

        answer.append(min(moved_values))

    return answer