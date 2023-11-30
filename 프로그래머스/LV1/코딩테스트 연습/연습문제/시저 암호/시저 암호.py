def solution(s, n):
    lower = ""
    upper = ""
    answer = ""

    for i in range(ord("a"), ord("z")+1):
        lower += chr(i)
        upper += chr(i - 32)
    
    lower += lower
    upper += upper
    
    for c in s:
        if c == ' ':
            answer += c
        else:
            if c.islower():
                answer += lower[lower.find(c) + n]
            else:
                answer += upper[upper.find(c) + n]
                
    return answer