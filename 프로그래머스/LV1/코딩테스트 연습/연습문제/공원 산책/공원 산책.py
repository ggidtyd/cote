def x_or_out(arr, cur_pos, direction, distance):
    a = 1
    if direction == 'W' or direction == 'N':
        if cur_pos - distance < 0:
            return True
        a = -1
    else:
        if cur_pos + distance >= len(arr):
            return True
        
    for i in range(1, distance+1):
        if arr[cur_pos + (a * i)] == 'X':
            return True
    return False


def is_valid_route(direction, distance, cur_loc, park, park_cols):
    if direction == 'W' or direction == 'E':
        if x_or_out(park[cur_loc[0]], cur_loc[1], direction, distance):
            return False
    else:
        if x_or_out(park_cols[cur_loc[1]], cur_loc[0], direction, distance):
            return False
    return True


def get_s(park, W, H):
    for r in range(H):
        for c in range(W):
            if park[r][c] == "S":
                return [r, c]
            

def solution(park, routes):
    W, H = len(park[0]), len(park)
    S = get_s(park, W, H)
    park_cols = [[park[r][c] for r in range(H)] for c in range(W)]
    
    cur_loc = S
    for route in routes:
        direction, distance = route[0], int(route[2])
        if is_valid_route(direction, distance, cur_loc, park, park_cols):
            if direction == "N":
                cur_loc[0] -= distance
            elif direction == "S":
                cur_loc[0] += distance
            elif direction == "E":
                cur_loc[1] += distance
            elif direction == "W":
                cur_loc[1] -= distance

    return cur_loc