def solution(n, words):
    answer = [0,0]
    used = set()
    before = words[0]
    used.add(words[0])

    for i in range(1, len(words)):
        if before[-1] != words[i][0] or words[i] in used:
            answer = [i%n+1, i//n+1]
            break
        used.add(words[i])
        before = words[i]
    return answer