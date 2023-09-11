def calc(r, in_or_out):
    cnt = 0
    for x in range(r):
        y = (r ** 2 - x ** 2) ** 0.5
        if in_or_out == "OUT":
            cnt += int(y)
        elif in_or_out == "IN":
            cnt += int(y) if y % 1 != 0 else int(y) - 1
    return cnt * 4 + 1


def solution(r1, r2):
    return calc(r2, "OUT") - calc(r1, "IN")