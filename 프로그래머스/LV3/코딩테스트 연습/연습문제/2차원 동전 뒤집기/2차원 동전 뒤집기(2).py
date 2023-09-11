def solution(beginning, target):
    answer = 0
    table = [[beginning[i][j] ^ target[i][j] for j in range(len(beginning[i]))] for i in range(len(beginning))]
    cnt = 0
    m = len(table)
    n = len(table[0])

    for i in range(1, m):
        if (table[i] != table[0]):
            cnt+=1
            if (list(map(lambda x: x ^ 1, table[i])) != table[0]):
                return -1

    answer = min((cnt) + sum(table[0]), (m - cnt) + (n - sum(table[0])))

    return answer