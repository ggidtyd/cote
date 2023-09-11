def solution(n, cores):
    left = 1
    right = max(cores) * n
    n -= len(cores)
    
    while left < right:
        mid = (left + right) // 2
        work = 0
        for core in cores:
            work += mid // core
            if work >= n:
                break
        
        if work >= n:
            right = mid
        else:
            left = mid + 1
            
    for core in cores:
        n -= (left-1) // core
        
    for i, core in enumerate(cores):
        if left % core == 0:
            n -= 1
            if n == 0:
                return i+1