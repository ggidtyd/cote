def solution(a):
    dic = {n : [0, -1] for n in list(set(a))}
    c = 0

    for i in range(len(a)):
        if i > 0 and dic[a[i]][1] != i-1 and a[i-1] != a[i]:
            dic[a[i]][0] += 1
            dic[a[i]][1] = i-1
        elif i < len(a)-1 and a[i] != a[i+1]:
            dic[a[i]][0] += 1
            dic[a[i]][1] = i+1
        c = max(c, dic[a[i]][0])

    return c * 2 if len(a) >= c * 2 else (len(a) - c) * 2