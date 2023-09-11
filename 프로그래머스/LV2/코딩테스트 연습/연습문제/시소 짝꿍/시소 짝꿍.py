def solution(weights):
    answer = 0
    dic = {w:0 for w in weights}

    for w in weights: dic[w] += 1

    for n in dic.values():
        if n >= 2: answer += (n * (n-1)) // 2

    for w in dic.keys():
        if w * (2 / 3) in dic: answer += dic[w] * dic[w * (2 / 3)]
        if w * (3 / 4) in dic: answer += dic[w] * dic[w * (3 / 4)]
        if w * (2 / 4) in dic: answer += dic[w] * dic[w * (2 / 4)]

    return answer