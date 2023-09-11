def get_distance(p1, p2):
    return (p1[0]-p2[0]) ** 2 + (p1[1]-p2[1]) ** 2


def solution(m, n, start_x, start_y, balls):
    answer = []

    for x, y in balls:
        min_d = 1001 * 1001 * 2
        temp = [[x, 2 * n - y], [x, y * -1], [x * -1, y], [2 * m - x, y]]
        
        for i, t in enumerate(temp):
            if y == start_y and x < start_x and i == 2: continue
            if y == start_y and x > start_x and i == 3: continue
            if x == start_x and y < start_y and i == 1: continue
            if x == start_x and y > start_y and i == 0: continue

            min_d = min(min_d, get_distance([start_x, start_y], [t[0], t[1]]))
        answer.append(min_d)
    return answer