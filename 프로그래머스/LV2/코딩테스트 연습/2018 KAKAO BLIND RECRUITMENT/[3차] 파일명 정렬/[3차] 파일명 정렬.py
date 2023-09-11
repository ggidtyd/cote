import re

def solution(files):
    dic = {}

    for file in files:
        HEAD, NUMBER = re.match(r'([^0-9]+)([0-9]{1,5})', file).groups()
        dic[file] = [HEAD.lower(), int(NUMBER)]

    tuples = sorted(dic.items(), key=lambda x:(x[1][0], x[1][1]))
    return [t[0] for t in tuples]