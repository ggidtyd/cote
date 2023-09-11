def solution(expression):
    ans = 0
    orders = ["*+-", "*-+","+*-", "+-*", "-*+", "-+*"]
    temp = ""
    nums = []
    op = []

    for c in expression:
        if (c == '+') or (c == '*') or (c == '-'):
            op.append(c)
            nums.append(int(temp))
            temp = ""
        else:
            temp += c
    nums.append(int(temp))

    for order in orders:
        temp_nums = nums.copy()
        temp_op = op.copy()
        for symbor in order:
            while temp_op:
                if symbor in temp_op:
                    i = temp_op.index(symbor)
                else:
                    break
                if symbor == '*':
                    temp_nums[i] = temp_nums[i] * temp_nums[i+1]
                    temp_nums.pop(i+1)
                elif symbor == '+':
                    temp_nums[i] = temp_nums[i] + temp_nums[i+1]
                    temp_nums.pop(i+1)
                elif symbor == '-':
                    temp_nums[i] = temp_nums[i] - temp_nums[i+1]
                    temp_nums.pop(i+1)
                temp_op.pop(i)
        ans = max(ans, abs(temp_nums[0]))
    return ans
    