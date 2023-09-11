def to_n(i, n):
    s = ''
    while i:
        i, r = divmod(i, n)
        if 10 <= r <= 15:
            s += chr(r+55)
        else:
            s += str(r)
    return s[::-1]


def solution(n, t, m, p):
    answer = ""
    s = "0"

    i = 1
    while len(s) < t*m:
        s += to_n(i, n)
        i += 1
    
    i = p-1
    while t:
        answer += s[i]
        i += m
        t -= 1
    return answer