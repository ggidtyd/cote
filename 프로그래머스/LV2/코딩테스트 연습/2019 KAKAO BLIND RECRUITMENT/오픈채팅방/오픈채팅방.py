def solution(record):
    answer = []
    enter_leave = []
    uid_name_dict = dict()

    for rec in record:
        if rec[0] == 'L':
            action, uid = rec.split(' ')
            enter_leave.append((action, uid))
            continue
        action, uid, name = rec.split(' ')
        if action == "Change":
            uid_name_dict[uid] = name
        elif action == "Enter":
            uid_name_dict[uid] = name
            enter_leave.append((action, uid))

    for el in enter_leave:
        action, uid = el[0], el[1]
        if action == "Enter":
            answer.append(f"{uid_name_dict[uid]}님이 들어왔습니다.")
        else:
            answer.append(f"{uid_name_dict[uid]}님이 나갔습니다.")
    return answer
