def solution(s):
    alphabet_idxs_dict = dict()
    answer = []
    for i in range(len(s)):
        if s[i] not in alphabet_idxs_dict:
            alphabet_idxs_dict[s[i]] = [i]
            answer.append(-1)
        else:
            answer.append(i - alphabet_idxs_dict[s[i]][-1])
            alphabet_idxs_dict[s[i]].append(i)
    return answer