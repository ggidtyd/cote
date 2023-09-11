def get_required_days(p, v):
    day = 0
    while p < 100:
        p += v
        day += 1
    return day

def solution(progresses, speeds):
    answer = []

    idx = 0
    len_of_prog = len(progresses)

    while idx < len_of_prog:
        required_days = get_required_days(progresses[idx], speeds[idx])
        items = 1
        for i in range(idx+1, len_of_prog):
            trd = get_required_days(progresses[i], speeds[i])
            if trd <= required_days:
                items += 1
            else:
                answer.append(items)
                idx += items
                break
        else:
            answer.append(items)
            idx += items
    return answer