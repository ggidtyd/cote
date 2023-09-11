def solution(name):
    answer = 0
    name_len = len(name)
    min_move = name_len - 1
    
    for i in range(name_len):
        answer += min(ord(name[i]) - ord('A'), ord('Z') + 1 - ord(name[i]))
        idx = i + 1

        while idx < name_len and name[idx] == 'A':
            idx += 1

        min_move = min(min_move, i * 2 + name_len - idx)
        min_move = min(min_move, (name_len - idx) * 2 + i)

    return answer + min_move

