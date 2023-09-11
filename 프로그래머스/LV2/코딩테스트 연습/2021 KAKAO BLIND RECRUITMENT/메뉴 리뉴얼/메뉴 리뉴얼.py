def courses_that_can_be_made_in_each_order(j, order, course, course_menu_num, courses):
    if len(course) == course_menu_num:
        courses.add("".join(sorted(course)))
        return

    for i in range(j, len(order)):
        courses_that_can_be_made_in_each_order(i+1, order, course+order[i], course_menu_num, courses)

def solution(orders, course):
    answer = []
    courses = set()
    order_sets = [set(order) for order in orders]
    dic = dict()

    for c in course:
        for order in orders:
            courses_that_can_be_made_in_each_order(0, order, "", c, courses)

    courses = list(courses)

    for course in courses:
        ordered_num = 0
        cur_course_set = set(course)
        for order_set in order_sets:
            if len(cur_course_set - order_set) == 0:
                ordered_num += 1

        if ordered_num < 2: continue

        if len(course) not in dic: dic[len(course)] = [(course, ordered_num)]
        elif ordered_num > dic[len(course)][0][1]: dic[len(course)] = [(course, ordered_num)]
        elif ordered_num == dic[len(course)][0][1]: dic[len(course)].append((course, ordered_num))
    
    for courses in list(dic.values()):
        for course in courses:
            answer.append(course[0])

    return sorted(answer)