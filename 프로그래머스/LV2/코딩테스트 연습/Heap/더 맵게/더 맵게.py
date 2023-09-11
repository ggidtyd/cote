from heapq import heapify, heappush, heappop

def cut_pos(scov, k):
    for i in range(len(scov)):
        if scov[i] >= k:
            break
    return i + 1

def solution(scoville, K):

    answer = 0
    scoville.sort()
    scoville = scoville[:cut_pos(scoville, K)]
    heapify(scoville)
    heap_size = len(scoville)

    while heap_size > 1:
        temp = scoville[0]
        heappop(scoville)
        temp += scoville[0] * 2
        heappop(scoville)

        heappush(scoville, temp)

        answer += 1
        heap_size -= 1

        if scoville[0] >= K:
            return answer

    if scoville[0] < K:
        answer = -1
    return answer

