def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for i, n in enumerate(numbers):
        while stack and stack[-1][0] < n:
            _, ans_idx = stack.pop()
            answer[ans_idx] = n
        stack.append((n, i))

    return answer