import heapq


def put(q, dp, tcost, key):
    if key not in dp or tcost < dp[key]:
        dp[key] = tcost
        heapq.heappush(q, (tcost, key))


def solution(alp, cop, problems):
    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]
    dp = {(alp, cop): 0}
    algoal = max(i[0] for i in problems)
    cogoal = max(i[1] for i in problems)
    q = [(0, (alp, cop))]

    while q[0][1][0] < algoal or q[0][1][1] < cogoal:
        ct, (cal, cco) = heapq.heappop(q)
        for alreq, coreq, alrwd, corwd, cost in problems:
            if cal >= alreq and cco >= coreq:
                put(q, dp, ct+cost, (min(cal+alrwd, 150), min(cco+corwd, 150)))
                
    return q[0][0]