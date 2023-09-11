def solution(dirs):
    answer = 0
    ways = set()
    cur_x,cur_y = 0,0
    next_x,next_y = cur_x,cur_y

    move = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    for d in dirs:
        next_x = cur_x + move[d][0]
        next_y = cur_y + move[d][1]

        if next_x < -5 or next_x > 5 or next_y < -5 or next_y > 5:
            continue

        way = f"{cur_x}{cur_y}{next_x}{next_y}"
        reverse_way = f"{next_x}{next_y}{cur_x}{cur_y}"
        if way not in ways and reverse_way not in ways:
            answer += 1
            ways.add(way)
        cur_x, cur_y = next_x, next_y
    return answer

