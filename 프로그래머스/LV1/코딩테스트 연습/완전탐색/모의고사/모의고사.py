def solution(answers):
    answer = []
    ones_answer_sheet = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    twos_answer_sheet = [2, 1, 2, 3, 2, 4, 2, 5]
    threes_answer_sheet = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    number_of_hits = [0, 0, 0]
    idx_of_1_3 = 0
    idx_of_2 = 0
    for ans in answers:
        if idx_of_1_3 == 10:
            idx_of_1_3 = 0
        if idx_of_2 == 8:
            idx_of_2 = 0
        if ans == ones_answer_sheet[idx_of_1_3]:
            number_of_hits[0] += 1
        if ans == twos_answer_sheet[idx_of_2]:
            number_of_hits[1] += 1
        if ans == threes_answer_sheet[idx_of_1_3]:
            number_of_hits[2] += 1
        idx_of_1_3 += 1
        idx_of_2 += 1

    max_hits_num = max(number_of_hits)

    for i in range(3):
        if number_of_hits[i] == max_hits_num:
            answer.append(i + 1)
    return answer
