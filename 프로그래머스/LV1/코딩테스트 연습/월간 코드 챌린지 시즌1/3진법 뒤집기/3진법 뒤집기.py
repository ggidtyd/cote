def reversed_3(n):
    ret = ""

    while n > 0:
        ret += str(n%3)
        n //= 3
    return ret


def solution(n):
    reversed_str_3 = reversed_3(n)
    answer = int(reversed_str_3,3)
    return answer