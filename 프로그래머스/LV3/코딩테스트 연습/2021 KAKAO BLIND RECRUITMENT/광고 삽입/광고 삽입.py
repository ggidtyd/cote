def to_sec(hhmmss):
    hh, mm, ss = hhmmss.split(':')
    return int(hh) * 3600 + int(mm) * 60 + int(ss)


def to_hhmmss(sec):
    hh = str(sec // 3600).zfill(2)
    sec %= 3600
    mm = str(sec // 60).zfill(2)
    sec %= 60
    ss = str(sec).zfill(2)
    return f"{hh}:{mm}:{ss}"


def solution(play_time, adv_time, logs):
    if play_time == adv_time:
        return "00:00:00"
    
    play_time, adv_time = to_sec(play_time), to_sec(adv_time)
    arr = [0] * (play_time+1)
    start, end = 101 * 3600, 0
    
    for log in logs:
        s, e = log.split('-')
        s, e = to_sec(s), to_sec(e)
        arr[s] += 1
        arr[e] -= 1
        start, end = min(start, s), max(end, e)
    
    for i in range(end):
        arr[i+1] += arr[i]
    
    left, right = 0, adv_time
    s = sum(arr[0:right])
    max_s = s
    answer = left

    for r in range(right, end):
        s -= arr[left]
        s += arr[r]
        left += 1

        if s > max_s:
            max_s = s
            answer = left

    return to_hhmmss(answer)