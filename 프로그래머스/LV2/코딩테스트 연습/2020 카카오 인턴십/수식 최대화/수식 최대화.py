import itertools

def excute_order(order, expr):
    e_last = []
    second = []
    third = expr.split(order[2])
    e = ""
    for t in third:
        second.append(t.split(order[1]))

    for s in second:
        if len(s) == 1:
            e_last.append(str(eval(s[0])))
        else:
            temp = ""
            for c in s:
                c = str(eval(c))
                temp += c + order[1]
            temp = temp.rstrip(order[1])
            e_last.append(str(eval(temp)))

    for f in e_last:
        e += f + order[2]
    e = e.rstrip(order[2])

    return abs(eval(e))

def solution(expression):
    ans = 0
    symbols = ['*', '+', '-']
    orders = itertools.permutations(symbols, 3)
    for order in orders:
        ans = max(ans, excute_order(order, expression))
    return ans