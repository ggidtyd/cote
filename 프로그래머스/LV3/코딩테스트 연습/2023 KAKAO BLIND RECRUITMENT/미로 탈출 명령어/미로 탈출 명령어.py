from collections import deque


def solution(n, m, x, y, r, c, k):
    q = deque([(0, (x, y), "")])
    
    dp = [["z"] * (m+1) for _ in range(n+1)]
    move = {'l':[0,-1], 'r':[0,1], 'u':[-1,0], 'd':[1,0]}
    
    while q:
        distance, point, path = q.popleft()
        
        if distance == k and point == (r, c):
            continue
            
        for direction, m in move.items():
            next_r, next_c = point[0] + m[0], point[1] + m[1]
            npath = path+direction
            if next_r < 1 or next_r > n or next_c < 1 or next_c > n: continue
            if distance+1 == k and (next_r, next_c) != (r, c): continue
            if dp[next_r][next_c] > npath:
                dp[next_r][next_c] = npath

            q.append((distance+1, (next_r, next_c), npath))
    
    if dp[r][c] == 'z':
        return -1
    return dp[r][c]