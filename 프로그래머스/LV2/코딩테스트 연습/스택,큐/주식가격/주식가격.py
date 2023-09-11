def solution(prices):
    answer = [i for i in range(len(prices)-1, -1, -1)]
    stack = []

    for i in range(len(prices)):
        while stack and stack[-1][1] > prices[i]:
            idx = stack.pop()[0]
            answer[idx] = i - idx

        stack.append([i, prices[i]])
    return answer