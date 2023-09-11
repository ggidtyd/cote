import numpy as np

def solution(N, stages):
    answer = []
    sn_fr_dict = {x: 0 for x in range(1,N+1)}

    np_stages = np.array(stages)
    d = len(stages)
    for n in range(1,N+1):
        if n not in stages:
            sn_fr_dict[n] = 0
        else:
            u = len(np.where(np_stages==n)[0])
            sn_fr_dict[n] = u / d
            d -= u

    reversed_by_value = sorted(sn_fr_dict, key=lambda x: sn_fr_dict[x], reverse=True)

    answer = reversed_by_value

    return answer