def solution(dots):
    
    for i in range(len(dots)):
        for j in range(i+1, len(dots)):
            o1, o2 = {0, 1, 2, 3} - {i, j}
            a1 = (dots[i][1] - dots[j][1]) / (dots[i][0] - dots[j][0])
            a2 = (dots[o1][1] - dots[o2][1]) / (dots[o1][0] - dots[o2][0])

            if a1 == a2:
                return 1
    return 0