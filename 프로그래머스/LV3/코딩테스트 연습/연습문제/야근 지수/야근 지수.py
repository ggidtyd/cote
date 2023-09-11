from heapq import heappush, heappop

def solution(n, works):
    heap = []
    for work in works:
        heappush(heap, (-work, work))

    while n and heap:
        m = heappop(heap)[1]
        if m == 0:
            continue
        heappush(heap, (-(m-1), (m-1)))
        n -= 1

    return sum([v[1] ** 2 for v in heap])