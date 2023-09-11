ans = 0

def go(select, sum, j, number):
    global ans
    if select == 3:
        if sum == 0:
            ans += 1
        return
    for i in range(j, len(number)):
        go(select+1, sum + number[i], i+1, number)

def solution(number):
    global ans
    go(0, 0, 0, number)
    return ans