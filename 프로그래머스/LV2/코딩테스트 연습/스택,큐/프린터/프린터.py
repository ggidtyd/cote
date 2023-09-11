from collections import deque

def solution(priorities, location):
    answer = 0
    lst = [(p, i) for i, p in enumerate(priorities)]
    q = deque(lst)

    while q:
        cur = q.popleft()
        if any(t[0] > cur[0] for t in q):
            q.append(cur)
        else:
            answer += 1
            if cur[1] == location:
                break

    return answer