def upper_lower(w):
    ret = ""
    i = 0
    for c in w:
        if i % 2 == 0:
            ret += c.upper()
        else:
            ret += c.lower()
        i += 1
    return ret

def solution(s):
    answer = []
    words = s.split(" ")

    for w in words:
        answer.append(upper_lower(w))
    return " ".join(answer)