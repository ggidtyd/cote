def solution(lines):
    answer = 1
    ranges = []

    for line in lines:
        _, s, t = line.split()
        end_time = int(s[:2]) * 3600 * 1000 + int(s[3:5]) * 60 * 1000 + int(float(s[6:]) * 1000)
        start_time = end_time - int(float(t[:-1]) * 1000) + 1
        ranges.append((start_time, end_time))

    for i in range(len(ranges)):
        cnt = 1
        for j in range(i+1, len(ranges)):
            if ranges[i][1] + 999 >= ranges[j][0]:
                cnt += 1
        answer = max(answer, cnt)
    return answer