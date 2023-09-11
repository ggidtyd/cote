def solution(price, money, count):
    total_price = price * (count * (count + 1)) // 2
    answer = money - total_price

    if answer >= 0:
        answer = 0
    else:
        answer = abs(answer)
    return answer