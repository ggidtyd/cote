def solution(sequence, k):
    n = len(sequence)
    s = [0] * (n+1)
    min_len = 1000001

    for i in range(n):
        s[i+1] = s[i] + sequence[i]

    left = 0
    right = 1

    while left < right <= n:
        partial_sum = s[right] - s[left]
        if partial_sum == k:
            partial_len = right - left
            if min_len > partial_len:
                answer = [left, right-1]
                min_len = partial_len
            
        if partial_sum < k:
            right += 1
        else:
            left += 1

    return answer

