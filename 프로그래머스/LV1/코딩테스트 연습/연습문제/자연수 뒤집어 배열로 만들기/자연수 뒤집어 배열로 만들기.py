def solution(n):
    answer = []
    reversed_n_str = str(n)[::-1]
    answer = list(map(int, reversed_n_str))
    return answer
    