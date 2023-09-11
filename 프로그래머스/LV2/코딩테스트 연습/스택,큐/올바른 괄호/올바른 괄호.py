def solution(s):
    stack = 0

    for c in s:
        stack += 1 if c == '(' else -1
        if stack < 0:
            return False

    return stack == 0