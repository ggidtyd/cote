def ipn(x):
    for i in range(2, int(x**(0.5))+1):
        if x % i == 0:
            return False
    return True

def find_start_numbers(n):
    ret = set()
    for i in range(2, int(n**(0.5)+1)):
        if ipn(i):
            ret.add(i)
    return ret

def solution(n):
    all_numbers = set(range(2, n+1)) 
    start_numbers = find_start_numbers(n)
    for sn in start_numbers:
        all_numbers -= set(range(2*sn, n+1, sn)) 
    return len(all_numbers)
