def solution(strings, n):
    nth_char_string_dict = {}
    nth_char_list = []
    answer = []
    
    for s in strings:
        if s[n] not in nth_char_string_dict:
            nth_char_string_dict[s[n]] = [s]
        else:
            nth_char_string_dict[s[n]].append(s)
            nth_char_string_dict[s[n]].sort()
        nth_char_list.append(s[n])
    
    nth_char_list.sort()
    
    for nth_char in nth_char_list:
        answer.append(nth_char_string_dict[nth_char].pop(0))
    return answer

print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))
