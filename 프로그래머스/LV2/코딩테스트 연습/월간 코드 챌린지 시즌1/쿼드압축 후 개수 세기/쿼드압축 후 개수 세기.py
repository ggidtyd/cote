def go(len, start_x, start_y, arr, result):
    sum = 0
    for r in range(start_x, start_x + len):
        for c in range(start_y, start_y + len):
            sum += arr[r][c]

    if sum == 0 or sum == len * len:
        result[arr[start_x][start_y]] += 1
        return

    for x in range(start_x, start_x + len, len // 2):
        for y in range(start_y, start_y + len, len // 2):
            go(len//2, x, y, arr, result)


def solution(arr):
    answer = {0:0, 1:0}
    go(len(arr), 0, 0, arr, answer)
    return [answer[0], answer[1]]