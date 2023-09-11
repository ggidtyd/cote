def solution(clothes):
    answer = 1
    dic = dict()

    for _, type in clothes:
        if type not in dic: dic[type] = 1
        else: dic[type] += 1

    for v in dic.values():
        answer *= (v+1)

    return answer-1

