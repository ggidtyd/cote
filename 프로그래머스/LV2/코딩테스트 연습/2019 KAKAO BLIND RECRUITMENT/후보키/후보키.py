import itertools

def append_ck(cols, ck, relation):
    temp = []
    for k in range(2, len(cols)+1):
        temp += itertools.combinations(cols, k)
        
    for col_combi in temp:
        combi = "".join(col_combi)
        if doesnt_have_ck(combi, ck) and key(combi, relation):
            ck.append(combi)

def doesnt_have_ck(selected_cols, candidate_key):
    for i in range(1,len(selected_cols)+1):
        combis = itertools.combinations(selected_cols, i)
        for combi in combis:
            if "".join(combi) in candidate_key:
                return False
    return True

def duplicate(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

def key(combi, relation):
    arr = []
    for t in relation:
        temp = []
        for s in combi:
            temp.append(t[int(s)])
        arr.append(temp)
    return not duplicate(arr)

def solution(relation):
    duplicate_cols = []
    candidate_key = []
    cols = []

    for i in range(len(relation[0])):
        cols.append([t[i] for t in relation])

    for i in range(len(relation[0])):
        if duplicate(cols[i]):duplicate_cols.append(str(i))
        else:candidate_key.append(str(i))

    append_ck(duplicate_cols, candidate_key, relation)

    return len(candidate_key)