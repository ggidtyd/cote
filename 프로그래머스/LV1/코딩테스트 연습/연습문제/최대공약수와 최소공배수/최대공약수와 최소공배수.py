def get_gcd(m,n):
    while n != 0:
       t = m%n
       (m,n) = (n,t)
    return abs(m)


def solution(n,m):
    gcd = get_gcd(n,m)
    return [gcd, n*m//gcd]