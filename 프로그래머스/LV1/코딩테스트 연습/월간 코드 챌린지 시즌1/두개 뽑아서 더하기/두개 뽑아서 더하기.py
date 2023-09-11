answer = set()
used = set()


def go(j, s, cnt, l, numbers):
    if cnt == 2:
        answer.add(s)
        return

    for i in range(j, l):
        if i in used:
            continue
        used.add(i)
        go(i+1, s+numbers[i], cnt+1, l, numbers)
        used.remove(i)


def solution(numbers):
    global answer
    go(0,0,0,len(numbers), sorted(numbers))

    return sorted(list(answer))


print(solution([5,0,2,7]))