def solution(s):
    answer = ''
    len_of_s = len(s)
    if len_of_s % 2 == 1:
        answer = s[len_of_s//2]
    else:
        answer = s[len_of_s//2-1:len_of_s//2+1]
    return answer