import re
from collections import Counter


def solution(s):
    return [int(t[0]) for t in sorted(Counter(re.findall('\d+', s)).items(), key=lambda x : x[1], reverse=True)]