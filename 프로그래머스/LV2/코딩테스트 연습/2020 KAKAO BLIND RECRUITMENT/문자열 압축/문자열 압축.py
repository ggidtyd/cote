def solution(s):
    answer = len(s)
    for unit_len in range(1, len(s) // 2 + 1):
        temp = ""
        cnt = 0
        unit = s[:unit_len]
        for i in range(0, len(s), unit_len):
            if s[i:i+unit_len] != unit:
                if cnt == 1: temp += unit
                else: temp += str(cnt) + unit
                unit = s[i:i+unit_len]
                cnt = 1
            else: cnt += 1
            
        if cnt == 1: temp += unit
        else: temp += str(cnt) + unit
        answer = min(len(temp), answer)
    return answer