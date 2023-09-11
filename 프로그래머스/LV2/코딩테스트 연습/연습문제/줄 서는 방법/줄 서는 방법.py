from math import factorial

def solution(n, k):
    answer = []
    numbers = [x for x in range(1, n+1)]
    number_idx = 0
    units = [factorial(x) for x in range(n)]
    unit_idx = n-1
    cnt = 0

    while unit_idx > 0:
        cnt += units[unit_idx]
        if cnt >= k:
            answer.append(numbers[number_idx])
            numbers.pop(number_idx)
            cnt -= units[unit_idx]
            unit_idx -= 1
            number_idx = 0
        else:
            number_idx += 1
    answer.append(numbers[number_idx])
    return answer