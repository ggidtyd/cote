import string


def solution(new_id):
    new_id = new_id.lower()

    symbols = string.punctuation.replace('-', '').replace('_', '').replace('.', '')
    for c in new_id:
        if c in symbols:
            new_id = new_id.replace(c, "")

    while ".." in new_id:
        new_id = new_id.replace("..", ".")

    new_id = new_id.lstrip(".")
    new_id = new_id.rstrip(".")

    if new_id == "":
        new_id = "a"

    if len(new_id) >= 16:
        new_id = new_id[0:15]
        new_id = new_id.rstrip(".")

    while len(new_id) <= 2:
        new_id += new_id[-1]

    answer = new_id
    return answer

