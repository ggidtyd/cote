def get_hail_progression(k):
    hail_progression = [k]
    while k != 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        hail_progression.append(k)
    return hail_progression

def solution(k, ranges):
    result = []
    hail_progression = get_hail_progression(k)
    hail_progression_end = len(hail_progression)-1
    for r in ranges:
        left = 0 + r[0]
        right = hail_progression_end + r[1]
        temp = 0 if left <= right else -1
        for i in range(left, right):
            temp += min(hail_progression[i],hail_progression[i+1])
            temp += abs(hail_progression[i]-hail_progression[i+1])/2
        result.append(temp)
    return result


print(solution(5, [[0,0],[0,-1],[2,-3],[3,-3]]))