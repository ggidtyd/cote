def solution(numbers):
    answer = []
    for n in numbers:
        b = 1
        temp = n
        while True:
            if temp & 1 == 0:
                break
            temp >>= 1
            b <<= 1
            
        answer.append(n + b - (b>>1))
    return answer
