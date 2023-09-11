ans = 0

def go(visit, dungeons, k, n):
    global ans
    if n > ans:
        ans = n

    for i in range(len(dungeons)):
        if not visit[i] and k >= dungeons[i][0]:
            visit[i] = True
            go(visit, dungeons, k - dungeons[i][1], n+1)
            visit[i] = False
    
def solution(k, dungeons):
    global ans
    visit = [False]*len(dungeons)
    go(visit, dungeons, k, 0)
    return ans