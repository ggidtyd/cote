def road_pavement(x):
    divisors = [1]

    if x == 1:
        return 0
        
    for i in range(2, int(x**0.5)+1):
        if x % i == 0 and x//i <= 10**7:
            divisors.append(x//i)
            break

    return max(divisors)


def solution(begin, end):
    return [road_pavement(i) for i in range(begin, end+1)]