from math import gcd
from functools import reduce

def func(arr1, arr2):
    g = reduce(gcd, arr1)
    for v in arr2:
        if v % g == 0:
            break
    else:
        return g
    return 0
                
def solution(arrayA, arrayB):
    return max(func(arrayA, arrayB), func(arrayB, arrayA))
