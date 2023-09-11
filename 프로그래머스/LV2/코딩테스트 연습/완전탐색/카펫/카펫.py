def get_whs(total):
    lst = []
    for i in range(1, int(total**(0.5))+1):
        if total % i == 0:
            lst.append((total // i, i))
    return lst


def solution(brown, yellow):
    answer = []
    whs = get_whs(brown + yellow)

    for wh in whs:
        if (wh[0]-2) * (wh[1]-2) == yellow:
            answer = [wh[0], wh[1]]
            break

    return answer
