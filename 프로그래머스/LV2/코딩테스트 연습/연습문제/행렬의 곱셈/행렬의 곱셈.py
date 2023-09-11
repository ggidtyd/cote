import numpy as np

def solution(arr1, arr2):
    return [list(map(int,r)) for r in np.array(arr1)@np.array(arr2)]
