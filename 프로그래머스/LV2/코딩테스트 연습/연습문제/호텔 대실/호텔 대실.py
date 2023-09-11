def to_minutes(hhmm):
    hh, mm = hhmm.split(':')
    return int(hh) * 60 + int(mm)


def solution(book_time):
    for i in range(len(book_time)):
        book_time[i][0] = to_minutes(book_time[i][0])
        book_time[i][1] = to_minutes(book_time[i][1])

    book_time.sort()
    rooms = [book_time[0]]

    for i in range(1, len(book_time)):
        for j in range(len(rooms)):
            if rooms[j][1] + 10 <= book_time[i][0]:
                rooms[j][1] = book_time[i][1]
                break
        else:
            rooms.append(book_time[i])
                
    return len(rooms)