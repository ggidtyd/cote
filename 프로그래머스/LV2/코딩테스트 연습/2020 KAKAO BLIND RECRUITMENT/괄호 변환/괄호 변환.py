def flip(u):
    ret = ""
    for c in u:
        if c == '(': ret += ')'
        else: ret += '('
    return ret


def correct_parenthesis(s):
    stack = []
    top = -1
    for c in s:
        if top != -1 and stack[top] == '(' and c == ')':
            stack.pop()
            top -= 1
        else:
            stack.append(c)
            top += 1
    
    return True if top == -1 else False
        

def go(w):

    if w == "": return ""

    num_of_open, num_of_close = 0, 0
    s, u, v = "", "", ""

    for i in range(len(w)):
        if w[i] == '(': num_of_open += 1
        elif w[i] == ')': num_of_close += 1
        
        if num_of_open == num_of_close:
            u = w[:i+1]
            v = w[i+1:]
            break

    if correct_parenthesis(u):
        u += go(v)
        return u
    else:
        s = "(" + go(v) + ")"
        s += flip(u[1:-1])
        return s

def solution(p):
    if correct_parenthesis(p):
        return p

    return go(p)