def solution(line):
    answer = []
    xs = []
    ys = []
    line_len = len(line)
    for i in range(line_len):
        for j in range(i+1, line_len):
            d = line[i][0]*line[j][1] - line[i][1]*line[j][0]
            if d == 0:
                continue
            xn = line[i][1]*line[j][2] - line[i][2]*line[j][1]
            yn = line[i][2]*line[j][0] - line[i][0]*line[j][2]
            x = xn / d
            y = yn / d
            if x.is_integer() and y.is_integer():
                xs.append(int(x))
                ys.append(int(y))

    min_x,max_x,min_y,max_y = min(xs), max(xs), min(ys), max(ys)
    xs = [x - min_x for x in xs]
    ys = [max_y - y for y in ys]

    row = max_y - (min_y-1)
    col = max_x - (min_x-1)

    for _ in range(row):
        answer.append(['.'] * col)
    for y, x in zip(ys,xs):
        answer[y][x] = '*'
    for r in range(row):
        answer[r] = "".join(answer[r])
    return answer