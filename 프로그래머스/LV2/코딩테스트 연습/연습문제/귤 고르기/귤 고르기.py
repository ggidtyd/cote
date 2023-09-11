def solution(k, tangerine):
    ans = 0
    dic = {i:0 for i in tangerine}

    for i in tangerine:
        dic[i] += 1

    sorted_dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)

    for t in sorted_dic:
        k -= t[1]
        ans += 1
        if k <= 0:
            break
    return ans