def solution(x, y):
    answer = ""
    intersection = set(x) & set(y)

    if len(intersection) == 0:
        return "-1"
    if len(intersection) == 1 and '0' in intersection:
        return "0"

    for c in intersection:
            answer += c * min(x.count(c), y.count(c))
    return "".join(sorted(answer, reverse=True))
