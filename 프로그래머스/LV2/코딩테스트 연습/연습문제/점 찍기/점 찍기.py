from math import sqrt

def solution(k, d):
    xs, ys = [], []

    for a in range(d//k+1):
        xs.append(a*k)
    
    for x in xs:
        ys.append(sqrt(d**2 - x**2) // k + 1)

    return sum(ys)