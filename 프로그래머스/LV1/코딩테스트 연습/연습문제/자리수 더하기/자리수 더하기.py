def solution(n):
    answer = 0
    n_str = str(n)
    for c in n_str:
        answer += int(c)
    return answer

print(solution(123))