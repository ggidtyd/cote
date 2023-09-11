from collections import deque

def solution(people, limit):
    ans = 0
    people.sort()
    
    q = deque(people)

    while len(q) > 1:
        if q[0] + q[-1] <= limit:
            q.popleft()
            q.pop()
        else:
            q.pop()
        ans += 1
    
    if q: ans += 1

    return ans
