import re
def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        st = re.sub(f'[^{skill}]','',st)
        if st == "" or st[0] == skill[0] and st in skill:
            answer += 1
    return answer