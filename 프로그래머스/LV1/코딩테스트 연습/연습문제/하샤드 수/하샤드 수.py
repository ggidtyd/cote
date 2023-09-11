


def get_sum_of_digits(s):
    ret = 0
    for c in s:
        ret += int(c)
    return ret

def is_big_joy(x):
    s = get_sum_of_digits(str(x))
    if x % s == 0:
        return True
    else:
        return False
    
def solution(x):
    answer = is_big_joy(x)
    return answer

print(solution(13))