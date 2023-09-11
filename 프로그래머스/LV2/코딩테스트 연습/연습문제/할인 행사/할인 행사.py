from collections import deque


def sign_up_day(want, dic, q):
    for w in want:
        if q.count(w) != dic[w]:
            return 0
    return 1


def solution(want, number, discount):
    answer = 0
    dic = {want[i]:number[i] for i in range(len(want))}
    q = deque(discount[:10])
    discount = discount[10:]
    discount = deque(discount)
    while discount:
        answer += sign_up_day(want, dic, q)
        q.popleft()
        q.append(discount.popleft())
    answer += sign_up_day(want, dic, q)
    return answer