from heapq import heapify, heappush, heappop

def solution(k, score):
    answer = []
    hall_of_fame = []
    heapify(hall_of_fame)

    for s in score:
        heappush(hall_of_fame, s)
        if len(hall_of_fame) > k:
            heappop(hall_of_fame)
            
        answer.append(hall_of_fame[0])
    return answer
