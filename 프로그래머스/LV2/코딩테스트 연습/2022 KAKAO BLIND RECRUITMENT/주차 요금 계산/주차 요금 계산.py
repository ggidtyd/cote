from math import ceil

def solution(fees, records):
    answer = []
    dic = dict()
    last_time = 23*60 + 59

    for record in records:
        time, car_number, inout = record.split(' ')
        h, m = time.split(':')
        time = int(h)*60 + int(m)
        car_number = int(car_number)

        if car_number not in dic:
            dic[car_number] = [[-time], inout]
        elif dic[car_number][1] == "IN":
            dic[car_number][0].append(time)
            dic[car_number][1] = inout
        elif dic[car_number][1] == "OUT":
            dic[car_number][0].append(-time)
            dic[car_number][1] = inout

    for k, v in dic.items():
        if v[1] == "IN":
            dic[k][0].append(last_time)
            dic[k][1] = "OUT"
        dic[k][0] = sum(dic[k][0])

    sorted_dic = sorted(dic.items(), key=lambda x:x[0])

    for info in sorted_dic:
        total_time = info[1][0]-fees[0]
        
        if total_time <= 0: answer.append(fees[1])
        else: answer.append(fees[1] + ceil(total_time/fees[2]) * fees[3])

    return answer
