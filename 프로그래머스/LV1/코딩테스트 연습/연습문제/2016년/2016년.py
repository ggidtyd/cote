month_day_dict = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
number_day_dict = {1:"FRI", 2:"SAT", 3:"SUN", 4:"MON", 5:"TUE", 6:"WED", 0:"THU"}


def solution(a, b):
    total_days_from_new_years_day = 0
    for m in range(1,a):
        total_days_from_new_years_day += month_day_dict[m]
    total_days_from_new_years_day += b

    answer = number_day_dict[total_days_from_new_years_day % 7]
    return answer
