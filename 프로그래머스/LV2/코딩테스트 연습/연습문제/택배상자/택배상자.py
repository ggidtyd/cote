def solution(order):
    stack = []
    order_pos = 0
    for i in range(1, len(order)+1):
        stack.append(i)
        while stack[-1] == order[order_pos]:
            order_pos += 1
            stack.pop()
            if len(stack) == 0:
                break
    return order_pos