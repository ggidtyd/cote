def collatz(x):
    cnt = 0
    while x != 1:
        if cnt >= 500:
            return -1

        if x % 2 == 0:
            x //= 2
        else:
            x *= 3
            x += 1
        cnt += 1
    return cnt

def solution(num):
    answer = collatz(num)
    return answer

print(solution(626331))