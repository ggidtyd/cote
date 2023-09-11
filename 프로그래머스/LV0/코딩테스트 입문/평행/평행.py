from itertools import combinations


def get_a(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (y2 - y1) / (x2 - x1)


def solution(dots):
    answer = 0
    pick2 = combinations([0, 1, 2, 3], 2)
    
    for i1, i2 in pick2:
        i3, i4 = {0, 1, 2, 3} - {i1, i2}
        
        l1_a = get_a(dots[i1], dots[i2])
        l2_a = get_a(dots[i3], dots[i4])
        
        if l1_a == l2_a:
            answer = 1
            break
        
    return answer