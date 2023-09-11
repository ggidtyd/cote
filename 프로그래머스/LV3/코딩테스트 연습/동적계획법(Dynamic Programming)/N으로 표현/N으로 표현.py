def solution(N, number):
    digit_count = 8

    expressions = [set() for _ in range(digit_count + 1)]

    for i in range(1, digit_count + 1):
        num_set = {int(str(N) * i)}

        for j in range(1, i):
            for x in expressions[j]:
                for y in expressions[i - j]:
                    num_set.add(x + y)
                    num_set.add(x - y)
                    num_set.add(x * y)

                    if y != 0:
                        num_set.add(x // y)

        expressions[i] = num_set

        if number in expressions[i]:
            return i

    return -1