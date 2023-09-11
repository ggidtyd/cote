import numpy as np

def solution(a, b):
    v1 = np.array(a)
    v2 = np.array(b)
    v3 = v1*v2
    return int(sum(v3))