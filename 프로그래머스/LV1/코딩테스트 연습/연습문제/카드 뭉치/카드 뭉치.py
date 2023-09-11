from collections import deque

def solution(cards1, cards2, goal):
    q1 = deque(cards1)
    q2 = deque(cards2)
    goal_idx = 0
    
    while q1 or q2:
        if goal_idx == len(goal): break
        
        if q1 and q1[0] == goal[goal_idx]:
            q1.popleft()
            goal_idx += 1
        elif q2 and q2[0] == goal[goal_idx]:
            q2.popleft()
            goal_idx += 1
        else:
            break
               
    return "Yes" if goal_idx == len(goal) else "No"