def solution(c):
    c.sort()
    cl = len(c)
    h = 0
    for i in range(cl):
        if c[i] >= cl-i:
            h = cl-i
            break
    return h