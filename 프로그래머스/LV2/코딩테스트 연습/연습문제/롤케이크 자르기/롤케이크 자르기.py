def solution(topping):
    answer = 0
    ln,rn = 0,len(set(topping))
    left = set()
    right = dict()
    for t in topping:
        if t not in right: right[t] = 1
        else: right[t] += 1

    for i in range(len(topping)-1):
        if i != 0 and ln == rn:
            answer += 1

        if topping[i] not in left:
            ln += 1
        left.add(topping[i])

        right[topping[i]] -= 1
        if right[topping[i]] == 0:
            rn -= 1

    return answer
