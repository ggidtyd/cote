def solution(ss):
    answer = []
    for s in ss:
        oneonezeros = 0
        new_s = []

        for c in s:
            if c == '0' and new_s[-2:] == ['1', '1']:
                oneonezeros += 1
                new_s.pop()
                new_s.pop()
            else:
                new_s.append(c)

        for i in range(len(new_s)-1, -1, -1):
            if new_s[i][-1] == '0':
                new_s[i] += "110" * oneonezeros
                break
        else:
            if len(new_s) == 0:
                new_s.append("110" * oneonezeros)
            else:
                new_s[0] = "110" * oneonezeros + new_s[0]
        
        s = "".join(new_s)
        answer.append(s)
    return answer