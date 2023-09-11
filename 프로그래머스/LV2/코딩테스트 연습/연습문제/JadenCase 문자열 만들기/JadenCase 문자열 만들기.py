answer = ""

def go(before, s, s_idx, s_len):
    global answer

    if s_idx == s_len:
        return

    if before.isdigit():
        answer += s[s_idx].lower()
    elif before == ' ':
        answer += s[s_idx].upper()
    else:
        answer += s[s_idx].lower()

    go(s[s_idx], s, s_idx+1, s_len)

def solution(s):
    global answer
    answer = s[0].upper() if s[0].isalpha() else s[0]
    go(s[0], s, 1, len(s))
    return answer