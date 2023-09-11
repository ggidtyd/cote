def solution(queue1, queue2):
    sum_of_q1 = sum(queue1)
    sum_of_q2 = sum(queue2)
    total_sum = sum_of_q1 + sum_of_q2
    firstlen = len(queue1)

    q12 = queue1 + queue2
    max_in_q1_q2 = max(q12)
    q12.remove(max_in_q1_q2)

    if max_in_q1_q2 > sum(q12) or total_sum % 2 != 0:
        return -1

    same_value = total_sum // 2
    cnt = 0
    front_of_q1 = 0
    front_of_q2 = 0

    while sum_of_q1 != same_value or sum_of_q2 != same_value:
        if front_of_q1 == firstlen*2 or front_of_q2 == firstlen*2:
            return -1

        if sum_of_q1 < same_value:
            move_value = queue2[front_of_q2]
            front_of_q2 += 1
            sum_of_q2 -= move_value
            sum_of_q1 += move_value
            
            queue1.append(move_value)
        else:
            move_value = queue1[front_of_q1]
            front_of_q1 += 1
            sum_of_q1 -= move_value
            sum_of_q2 += move_value
            
            queue2.append(move_value)
        cnt += 1
    return cnt
