def solution(name, yearning, photos):
    answer = []
    dic = {n : y for n, y in zip(name, yearning)}
    
    for photo in photos:
        temp = 0
        for name in photo:
            if name not in dic: continue
            temp += dic[name]
        answer.append(temp)

    return answer