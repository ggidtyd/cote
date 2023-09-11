from collections import deque


def hhmm_to_minute(hhmm):
    hh, mm = hhmm.split(':')
    return int(hh) * 60 + int(mm)


def minute_to_hhmm(minute):
    hh = str(minute // 60)
    mm = str(minute % 60)
    hhmm = f"{hh.zfill(2)}:{mm.zfill(2)}"
    return hhmm


def solution(n, t, m, timetable):
    answer = ''
    time = 540
    timetable.sort()
    q = deque(timetable)
    bus = []

    for bat in range(n):
        if not q: break
        bus = []
        for _ in range(m):
            if not q: break
            if hhmm_to_minute(q[0]) > time:
                break
            bus.append(q.popleft())

        if bat == n-1:
            break

        time += t

    if len(bus) == m:
        answer = minute_to_hhmm(hhmm_to_minute(bus[-1]) - 1)
    else:
        answer = minute_to_hhmm(time)

    return answer