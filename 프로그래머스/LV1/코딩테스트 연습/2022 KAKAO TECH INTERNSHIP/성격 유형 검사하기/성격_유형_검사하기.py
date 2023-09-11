def solution(survey, choices):
    answer = ''
    candidates = []
    indicator_type = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    indicator_score_dict = {
        'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0,
        'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0
    }
    
    idx_of_survey = 0
    
    for choice in choices:
        if choice > 4:
            indicator_score_dict[survey[idx_of_survey][1]] += choice - 4
        elif choice < 4:
            indicator_score_dict[survey[idx_of_survey][0]] += 4 - choice
        idx_of_survey += 1
    
    for type in survey:
        if indicator_score_dict[type[0]] > indicator_score_dict[type[1]]:
            candidates.append(type[0])
        elif indicator_score_dict[type[0]] < indicator_score_dict[type[1]]:
            candidates.append(type[1])
        else:
            candidates.append(sorted(type)[0])
    
    for it in indicator_type:
        if it[0] in candidates:
            answer += it[0]
        elif it[1] in candidates:
            answer += it[1]
        else:
            answer += it[0]
    return answer