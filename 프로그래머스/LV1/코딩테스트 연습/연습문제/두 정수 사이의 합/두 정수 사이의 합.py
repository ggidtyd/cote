def solution(a, b):
    answer = 0
    big_number = max(a,b)
    small_number = min(a,b)
    
    one_to_big = big_number*(big_number+1) // 2
    one_to_small = (small_number-1)*(small_number) // 2
    answer = one_to_big - one_to_small
    
    return answer
