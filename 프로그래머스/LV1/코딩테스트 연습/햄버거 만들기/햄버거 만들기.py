def solution(ingredient):
    answer = 0
    stack = [0] * len(ingredient)
    top = 0

    for i in range(len(ingredient)):
        stack[top] = ingredient[i]
        top += 1

        if top >= 3 and stack[top-4:top] == [1,2,3,1]:
            answer += 1
            top -= 4
            
    return answer

