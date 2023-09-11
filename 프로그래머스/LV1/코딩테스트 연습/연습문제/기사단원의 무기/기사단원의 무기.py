def get_number_of_divisors(n):
    ret = 0
    for i in range(1, int(n**0.5) + 1):
        if i*i == n:
            ret += 1
        elif n % i == 0:
            ret += 2

    return ret

def solution(number, limit, power):
    powers = [get_number_of_divisors(i) for i in range(1,number+1)]
    return sum([power if p > limit else p for p in powers])