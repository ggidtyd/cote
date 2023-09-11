def solution(dartResult):
    answer = []
    temp = 0
    num = ""
    for c in dartResult:
        if c.isdigit():
            num += c
        else:
            if num != "":
                temp = int(num)
                num = ""
            if c == "S":
                answer.append(temp)
            elif c == "D":
                answer.append(temp**2)
            elif c == "T":
                answer.append(temp**3)
            elif c == "*":
                if len(answer) == 1:
                    answer[0] *= 2
                else:
                    answer[-1] *= 2
                    answer[-2] *= 2
            elif c == "#":
                answer[-1] *= -1
    return sum(answer)



