import numpy as np

def find_not_0_idx(arr):
    for i in range(len(arr)):
        if arr[i] != 0:
            return i
    return -1

def solution(board, moves):
    answer = 0
    basket = []
    M = np.array(board)
    MT = M.T

    for move in moves:
        idx = find_not_0_idx(MT[move-1])
        if idx == -1:
            continue
        
        if len(basket) != 0 and MT[move-1][idx] == basket[-1]:
            answer += 2
            basket.pop()
        else:
            basket.append(MT[move-1][idx])
        MT[move-1][idx] = 0
    return answer