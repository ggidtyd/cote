MAX = 201 ** 201

def dp(i, j, mat, memo):
    if memo[i][j] != MAX:
        return memo[i][j]
    
    if j - i == 1:
        return 0

    for k in range(i+1, j):
        last = mat[i][0] * mat[k][0] * mat[j-1][1]
        memo[i][j] = min(memo[i][j], dp(i, k, mat, memo) + dp(k, j, mat, memo) + last)

    return memo[i][j]


def solution(matrix):
    n = len(matrix)
    memo = [[MAX] * (n+1) for _ in range(n+1)]
    return dp(0, n, matrix, memo)