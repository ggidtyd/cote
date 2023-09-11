left_hand_set = {1,4,7}
rigth_hand_set = {3,6,9}


keypad_xy_dic = {
    1 : (0,3),
    2 : (1,3),
    3 : (2,3),
    4 : (0, 2),
    5 : (1, 2),
    6 : (2, 2),
    7 : (0, 1),
    8 : (1, 1),
    9 : (2, 1),
    0 : (1, 0)
}

def solution(numbers, hand):
    answer = ""
    left_distance = 0
    right_distance = 0
    rh_xy = (2,0)
    lh_xy = (0,0)

    for n in numbers:
        next_xy = keypad_xy_dic[n]
        if n in left_hand_set:
            answer += "L"
            lh_xy = next_xy
        elif n in rigth_hand_set:
            answer += "R"
            rh_xy = next_xy
        else:
            left_distance = abs(next_xy[0] - lh_xy[0]) + abs(next_xy[1] - lh_xy[1])
            right_distance = abs(next_xy[0] - rh_xy[0]) + abs(next_xy[1] - rh_xy[1])
            if left_distance > right_distance:
                answer += "R"
                rh_xy = next_xy
            elif left_distance < right_distance:
                answer += "L"
                lh_xy = next_xy
            else:
                if hand == "right":
                    answer += "R"
                    rh_xy = next_xy
                else:
                    answer += "L"
                    lh_xy = next_xy
    return answer
