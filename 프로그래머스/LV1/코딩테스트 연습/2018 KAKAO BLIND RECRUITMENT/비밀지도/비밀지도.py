def decoding(x, n):
    ret = [" "] * n
    for i in range(n-1,-1,-1):
        if x % 2 == 1:
            ret[i] = "#"
        x //= 2
    return "".join(ret)


def solution(n, arr1, arr2):
    answer = []
    answer_number_version = []

    for i in range(n):
        answer_number_version.append(arr1[i] | arr2[i])
    for anv in answer_number_version:
        answer.append(decoding(anv, n))
    return answer