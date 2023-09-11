import numpy as np

def solution(arr1, arr2):
    m1 = np.array(arr1)
    m2 = np.array(arr2)
    answer = m1 + m2
    return answer.tolist()