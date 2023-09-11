def solution(participant, completion):
    answer = ''
    p_dic = {}
    c_dic = {}
    for p in participant:
        p_dic[p] = 0
    for c in completion:
        c_dic[c] = 0

    for p in participant:
        p_dic[p] += 1
    for c in completion:
        c_dic[c] += 1

    for k, v in c_dic.items():
        p_dic[k] -= c_dic[k]

    for k, v in p_dic.items():
        if p_dic[k] != 0:
            answer = k
    return answer