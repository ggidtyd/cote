def go(frm, to, n, ans):
    if n == 0:
        return

    other = 6 - frm - to
    go(frm, other, n - 1, ans)
    ans.append([frm, to])
    go(other, to, n - 1, ans)
    
def solution(n):
    ans = []
    go(1, 3, n, ans)
    return ans