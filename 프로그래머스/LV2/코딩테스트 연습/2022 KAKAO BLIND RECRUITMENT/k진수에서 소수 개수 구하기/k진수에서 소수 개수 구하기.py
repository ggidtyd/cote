def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int((x**0.5)) + 1):
        if x % i == 0:
            return False
    return True

def to_k(n, k):
    s = ''
    while n:
        n, r = divmod(n, k)
        s += str(r)
    return s[::-1] 

def solution(n, k):
    answer = 0
    kstr = to_k(n,k)
    if '0' not in kstr:
        return 1 if is_prime_number(int(kstr)) else 0
    
    by_0 = kstr.split('0')
    for s in by_0:
        if s == '' or is_prime_number(int(s)) == False:
            continue
        answer += 1
    return answer