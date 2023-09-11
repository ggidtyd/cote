def solution(n, m, section):
    wall = [False] * (n+1)
    for s in section:
        wall[s] = True

    answer = 0
    temp = section[0]

    for i in range(1, len(section)):
        if section[i] - temp >=  m:
            answer += 1
            temp = section[i]

    answer += 1

    return answer