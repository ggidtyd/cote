def solution(s):
    stack = []
    top = -1
    for c in s:
        if top != -1 and stack[top] == c:
            stack.pop()
            top -= 1
        else:
            stack.append(c)
            top += 1
    return 1 if top == -1 else 0 