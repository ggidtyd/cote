def solution(s):
    cnt, removed = 0, 0

    while len(s) > 1:
        temp = s.replace('0', '')
        removed += len(s) - len(temp)
        s = format(len(temp), 'b')
        cnt += 1

    return [cnt, removed]