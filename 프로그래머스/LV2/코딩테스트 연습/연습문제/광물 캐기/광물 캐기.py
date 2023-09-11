answer = 25 * 51
table = {"diamond" : {"diamond" : 1, "iron" : 1, "stone" : 1},
         "iron" : {"diamond" : 5, "iron" : 1, "stone" : 1},
         "stone" : {"diamond" : 25, "iron" : 5, "stone" : 1}}


def go(i, l, minerals, tools, cnts, fatigue):
    global table, answer
    if i >= l or (cnts[0] == 0 and cnts[1] == 0 and cnts[2] == 0):
        answer = min(answer, fatigue)
        return
    
    for j, picked in enumerate(tools):
        if cnts[j] == 0: continue
        temp = 0
        for mineral in minerals[i:i+5]:
            temp += table[picked][mineral]
        cnts[j] -= 1
        go(i+5, l, minerals, tools, cnts, fatigue+temp)
        cnts[j] += 1


def solution(picks, minerals):
    global answer
    tools = ["diamond", "iron", "stone"]
    go(0, len(minerals), minerals, tools, picks, 0)
    return answer