def solution(keymap, targets):
    answer = []

    dic = {chr(v):-1 for v in range(ord('A'), ord('Z')+1)}

    for c in dic.keys():
        temp = []
        for km in keymap:
            i = km.find(c)
            if i != -1:
                temp.append(i)
        if len(temp) > 0:
            dic[c] = min(temp) + 1
    
    
    for target in targets:
        cnt = 0
        for c in target:
            if dic[c] == -1:
                cnt = -1
                break
            else:
                cnt += dic[c]
        answer.append(cnt)
    return answer