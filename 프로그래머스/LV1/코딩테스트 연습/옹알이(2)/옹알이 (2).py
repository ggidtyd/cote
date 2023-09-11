def solution(babbling):
    answer = 0
    continuous_pronunciation = False
    can_speak = ["aya", "ye", "woo", "ma"]

    for b in babbling:
        for cs in can_speak:
            continuous_pronunciation = True if cs * 2 in b else False

            if continuous_pronunciation:
                break
            
            b = b.replace(cs, '-')
        
        if continuous_pronunciation == False:
            if set(b) == {'-'}:
                answer += 1
    return answer
