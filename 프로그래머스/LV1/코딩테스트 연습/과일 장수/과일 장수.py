def solution(k, m, score):
    return sum([s for s in sorted(score)[len(score) % m::m]])*m



# def solution(k, m, score):
#     score.sort(reverse=True)
#     return sum([score[i] for i in range(m-1, (len(score) // m) * m + 1, m)])*m