ans = [0]*11
max_diff = 0

def check_low_score(lion):
    for i in range(10, -1, -1):
        if lion[i] > ans[i]:return True
        elif lion[i] < ans[i]:return False

def go(j, cnt, n, apeach, lion):
    global ans, max_diff
    
    if cnt == n:
        lion_score, apeach_score = 0, 0

        for i in range(11):
            if lion[i] > apeach[i]:lion_score += 10-i
            elif apeach[i] != 0:apeach_score += 10-i

        diff = lion_score-apeach_score
        if diff > max_diff:
            max_diff = diff
            ans = lion.copy()
        elif diff == max_diff:
            if check_low_score(lion):
                ans = lion.copy()
        return

    for i in range(j, 11):
        lion[i] += 1
        if lion[i] > apeach[i]:
            go(i+1, sum(lion), n, apeach, lion)
        else:
            go(i, sum(lion), n, apeach, lion)
        lion[i] = 0

def solution(n, info):
    global ans, max_diff
    for i in range(11):
        go(i, 0, n, info, [0]*11)
    if max_diff == 0:ans = [-1]
    return ans