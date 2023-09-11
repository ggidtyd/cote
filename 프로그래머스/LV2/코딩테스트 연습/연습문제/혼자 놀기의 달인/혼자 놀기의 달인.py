def go(cards, idx, open, cnt):
    ret = 0
    if open[idx]: return cnt

    open[idx] = True
    ret = go(cards, cards[idx]-1, open, cnt + 1)

    return ret

def solution(cards):
    result = []
    open = [False] * len(cards)
    for i in range(len(cards)):
        if open[i]: continue
        result.append(go(cards, i, open, 0))

    result.sort(reverse=True)
    if len(result) == 1:
        return 0

    return result[0]*result[1]