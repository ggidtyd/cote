def solution(s):
    answer = 0
    s_len = len(s)
    s += s
    for i in range(s_len):
        temp = s[i:i+s_len]
        stack = ""
        for c in temp:
            stack += c
            if len(stack) >= 2 and ((ord(stack[-1]) - ord(stack[-2]) == 1) or (ord(stack[-1]) - ord(stack[-2]) == 2)):
                stack = stack[:-2]
        if stack == "":
            answer += 1
    return answer
