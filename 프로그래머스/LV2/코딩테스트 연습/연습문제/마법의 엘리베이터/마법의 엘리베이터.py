def solution(storey):
    if storey < 5:
        return storey

    r = storey % 10
    m = (storey - r) / 10

    return min(r + solution(m), 10 - r + solution(m + 1))