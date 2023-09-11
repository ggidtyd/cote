def get_point_pairs_less_than_distace2(rcs):
    point_pairs = []
    for i in range(len(rcs)):
        for j in range(i+1, len(rcs)):
            if abs(rcs[i][0] - rcs[j][0]) + abs(rcs[i][1] - rcs[j][1]) <= 2:
                point_pairs += [(rcs[i], rcs[j])]
    return point_pairs


def is_distancing(pp, place):
    for p1, p2 in pp:
        min_x, max_x = min(p1[0], p2[0]), max(p1[0], p2[0])
        min_y, max_y = min(p1[1], p2[1]), max(p1[1], p2[1])
        if min_x == max_x:
            if place[min_x][min_y+1] != 'X':
                return False
        elif min_y == max_y:
            if place[min_x+1][min_y] != 'X':
                return False
        else:
            if min_x == p1[0]:
                if place[min_x+1][p1[1]] != 'X' or place[max_x-1][p2[1]] != 'X':
                    return False
            else:
                if place[min_x+1][p2[1]] != 'X' or place[max_x-1][p1[1]] != 'X':
                    return False              
    return True


def solution(places):
    answer = []
    R, C = 5, 5

    for place in places:
        rcs = []
        for r in range(R):
            for c in range(C):
                if place[r][c] == 'P':
                    rcs.append((r, c))
        point_pairs = get_point_pairs_less_than_distace2(rcs)
        if len(point_pairs) == 0 or is_distancing(point_pairs, place): answer.append(1)
        else: answer.append(0)
    return answer