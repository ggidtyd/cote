def solution(n):
    answer = []
    map = [[0]*n for _ in range(n)]
    i, direction, r_start, c_start = 1, 0, 0, 0

    for l in range(n, 0, -1):
        if direction % 3 == 0:
            for r_start in range(l):
                map[r_start+r_start][c_start] = i
                i += 1
            c_start += 1
        elif direction % 3 == 1:
            for c_start in range(l):
                map[r_start+l][c_start+c_start] = i
                i += 1
            r_start += 1
        elif direction % 3 == 2:
            for di in range(1,l+1):
                map[r_start+l-di][c_start+l-di] = i
                i += 1
            r_start += 1
        direction += 1

    for r_start in map:
        for i in r_start:
            if i == 0:
                break
            answer.append(i)
    return answer

print(solution(4))