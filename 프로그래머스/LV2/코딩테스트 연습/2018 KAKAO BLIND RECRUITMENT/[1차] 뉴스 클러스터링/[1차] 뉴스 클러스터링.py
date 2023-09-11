def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    A = [str1[i:i+2] for i in range(len(str1)-1) if str1[i].isalpha() and str1[i+1].isalpha()]
    B = [str2[i:i+2] for i in range(len(str2)-1) if str2[i].isalpha() and str2[i+1].isalpha()]
    AS = set(A)
    BS = set(B)
    intersection = AS & BS
    union = AS | BS
    numerator = sum([min(A.count(ab), B.count(ab)) for ab in intersection])
    denominator = sum([max(A.count(ab), B.count(ab)) for ab in union])

    JAB = 1 if denominator == 0 and numerator == 0 else numerator / denominator
    return int(JAB * 65536)