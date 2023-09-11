def solution(s):
    answer = ''
    s = sorted(s)
    for c in s:
        if s.count(c) == 1:
            answer += c
    return answer