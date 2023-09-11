def solution(s, n):
    lower = ""
    upper = ""
    answer = ""

    for i in range(ord("a"), ord("z")+1):
        lower += chr(i)
        upper += chr(i-32)
    
    for c in s:
        if c.isalpha() and c.islower():
            new_idx = lower.find(c) + n
            if new_idx >= 26:
                new_idx -= 26
            answer += lower[new_idx]
        elif c.isalpha() and c.isupper():
            new_idx = upper.find(c) + n
            if new_idx >= 26:
                new_idx -= 26    
            answer += upper[new_idx]
        else:
            answer += c
    return answer