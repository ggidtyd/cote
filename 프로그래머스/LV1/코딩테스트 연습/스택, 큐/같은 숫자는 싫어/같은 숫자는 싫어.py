def solution(arr):
    answer = []
    cur_v = -1

    for v in arr:
        if cur_v == -1:
            answer.append(v)
            cur_v = v
            continue
        if cur_v == v:
            continue
        else:
            answer.append(v)
            cur_v = v
    return answer