class User:
    want_discount_ratio = 0
    signup_price = 0
    purchase_amount = 0

    def __init__(self, r, p):
        self.want_discount_ratio = r
        self.signup_price = p


def go(drs, cnt, end, selected, users, emoticons, result):
    if cnt == end:
        for user in users: user.purchase_amount = 0

        temp = []
        for i in range(len(emoticons)):
            temp.append(emoticons[i] * (100 - selected[i]) // 100)

        signup, profit = 0, 0

        for user in users:
            for i in range(len(temp)):
                if selected[i] >= user.want_discount_ratio:
                    user.purchase_amount += temp[i]

            if user.purchase_amount >= user.signup_price:
                signup += 1
                user.purchase_amount = 0

            profit += user.purchase_amount

        result.append([signup, profit])
        return

    for dr in drs:
        selected.append(dr)
        go(drs, cnt+1, end, selected, users, emoticons, result)
        selected.pop()


def solution(_users, emoticons):
    drs = [10, 20, 30, 40]
    users = []
    result = []

    for wdr, sp in _users:
        users.append(User(wdr, sp))

    go(drs, 0, len(emoticons), [], users, emoticons, result)
    result.sort(key=lambda x:(x[0], x[1]), reverse=True)
    return result[0]



