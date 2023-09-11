from collections import deque

def solution(N, road, K):
    dic = {i:[] for i in range(1,N+1)}
    times = [5000001] * (N+1)

    for data in road:
        city1, city2, time = data
        dic[city1].append((city2, time))
        dic[city2].append((city1, time))

    q = deque([[1, 0]])

    while q:
        cur_city, time = q.popleft()

        times[cur_city] = min(times[cur_city], time)

        connections = dic[cur_city]
        for next_city, t in connections:
            if times[next_city] < time: continue
            if time+t > K : continue
            q.append([next_city, time+t])
    
    return sum([1 for t in times if t <= K])