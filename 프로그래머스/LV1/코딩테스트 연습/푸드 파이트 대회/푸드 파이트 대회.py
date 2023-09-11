def solution(food):
    front = "".join([str(i) * (food[i] // 2) for i in range(len(food))])
    return front + "0" + front[::-1]