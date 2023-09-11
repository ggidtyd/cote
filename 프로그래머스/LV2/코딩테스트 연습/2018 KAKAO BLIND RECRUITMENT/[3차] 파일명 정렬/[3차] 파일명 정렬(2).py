def solution(files):
    dic = {}
    HEAD, NUMBER = "", ""
    head_end, number_end = 0, 0

    for file in files:
        for i in range(len(file)):
            if file[i].isdigit():
                head_end = i
                break
        
        number_end = min(head_end + 5, len(file))
        for i in range(head_end, number_end):
            if not file[i].isdigit():
                number_end = i
                break

        HEAD = file[:head_end]
        NUMBER = int(file[head_end:number_end])

        dic[file] = [HEAD.lower(), NUMBER]

    sorted_result = sorted(dic.items(), key=lambda x:(x[1][0], x[1][1]))

    return [t[0] for t in sorted_result]