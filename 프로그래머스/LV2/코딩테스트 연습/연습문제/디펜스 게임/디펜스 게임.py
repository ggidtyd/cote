from heapq import heappush, heappop

def solution(n, k, enemy):
    heap = []
    sum = 0
    
    for i in range(len(enemy)):
        heappush(heap, enemy[i])

        if len(heap) > k:
            sum += heap[0]
            heappop(heap)

        if sum > n:
            return i

    return len(enemy)
