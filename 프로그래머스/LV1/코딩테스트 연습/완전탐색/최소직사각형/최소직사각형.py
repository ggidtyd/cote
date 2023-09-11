def solution(sizes):
    answer = 0
    w = []
    h = []
    
    for s in sizes:
        w.append(max(s))
        h.append(min(s))
    
    answer = max(w) * max(h)
            
    return answer