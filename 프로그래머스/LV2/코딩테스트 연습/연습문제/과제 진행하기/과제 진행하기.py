from collections import deque


def hhmm_to_minute(hhmm):
    return int(hhmm[:2]) * 60 + int(hhmm[3:])


def solution(plans):
    answer, paused = [], []

    for i in range(len(plans)):
        plans[i][1] = hhmm_to_minute(plans[i][1])
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x:x[1])

    q = deque(plans)
    prog = q.popleft()
    
    while q:
        p_end = prog[1] + prog[2]
        if p_end <= q[0][1]:
            answer.append(prog[0])
            if paused and p_end < q[0][1]:
                paused[-1][1] = p_end
                prog = paused.pop()
            else:
                prog = q.popleft()
        else:
            prog[2] = p_end - q[0][1]
            paused.append(prog)
            prog = q.popleft()
    
    answer.append(prog[0])
    while paused:
        answer.append(paused.pop()[0])

    return answer