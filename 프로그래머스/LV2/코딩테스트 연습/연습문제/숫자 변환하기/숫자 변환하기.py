def solution(x, y, n):
    cnt = 0
    cur = set([x])

    while cur:
        if y in cur:
            return cnt
        next = set()
        for v in list(cur):
            if v * 2 <= y: next.add(v * 2)
            if v * 3 <= y: next.add(v * 3)
            if v + n <= y: next.add(v + n)
        cur = next
        cnt += 1
    return -1
