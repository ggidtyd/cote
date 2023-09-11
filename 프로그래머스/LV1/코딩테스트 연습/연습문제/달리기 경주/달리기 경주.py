def solution(players, callings):
    pi, ip = dict(), dict()
    for i, p in enumerate(players):
        pi[p] = i
        ip[i] = p

    for p in callings:
        f = ip[pi[p]-1]
        pi[p] -= 1
        pi[f] += 1
        ip[pi[p]], ip[pi[f]] = p, f
    
    return [ip[i] for i in range(len(players))]