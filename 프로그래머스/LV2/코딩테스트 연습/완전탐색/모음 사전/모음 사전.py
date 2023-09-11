previous_count = {'A' : 0, 'E' : 1, 'I' : 2, 'O' : 3, 'U' : 4}

def solution(word):
    answer = 0
    for i, n in enumerate(word):
        answer += ((5 * (5**(4-i) - 1) // 4) + 1) * previous_count[n] + 1
    return answer