def solution(elements):
    answer = set()

    elements_len = len(elements)
    sums = [0] * elements_len

    for i in range(elements_len-1):
        for j in range(elements_len):
            sums[j] += elements[(i+j) % elements_len]

        for s in sums:
            answer.add(s)

    return len(answer) + 1


