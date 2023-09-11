def go(numbers, target, i, s):
    ans = 0

    if i == len(numbers):
        if s == target:
            return 1
        return 0
    
    ans += go(numbers, target, i+1, s+numbers[i])
    ans += go(numbers, target, i+1, s-numbers[i])
    return ans

def solution(numbers, target):    
    return go(numbers, target, 0, 0)
