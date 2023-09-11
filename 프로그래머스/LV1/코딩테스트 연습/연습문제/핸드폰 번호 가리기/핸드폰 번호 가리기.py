def hide_phone_number(phone_number):
    hide_part = phone_number[:-4]
    phone_number = phone_number.replace(hide_part, "*"*len(hide_part))
    return phone_number

def solution(phone_number):
    answer = hide_phone_number(phone_number)
    return answer