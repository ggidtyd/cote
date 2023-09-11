from itertools import permutations

def is_prime_number(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    record = set()
    for i in range(1, len(numbers)+1):
        for card in permutations(numbers, i):
            card = int("".join(card))
            if card not in record and is_prime_number(card):
                answer += 1
                record.add(card)
    return answer

