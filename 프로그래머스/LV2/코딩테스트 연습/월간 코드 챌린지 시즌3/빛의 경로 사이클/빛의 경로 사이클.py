import sys
sys.setrecursionlimit(1500000)

def solution(grid):
    d_record = []
    path_lens = []
    row, col = len(grid), len(grid[0])
    directions = [[0,-1],[1,0],[0,1],[-1,0]]
    directions_len = len(directions)
    pathlen = 1

    for r in range(row):
        temp = []
        for c in range(col):
            temp.append(set())
        d_record.append(temp)
    
    def go(r, c, di, start, pathlen):
        if grid[r][c] == 'L':
            di = ((di+1)+directions_len) % directions_len
        elif grid[r][c] == 'R':
            di = ((di-1)+directions_len) % directions_len
            
        new_d = directions[di]

        newd_str = "".join(map(str,new_d))
        if newd_str in d_record[r][c]: return
        else: d_record[r][c].add(newd_str)

        if [r,c, new_d] == start:
            path_lens.append(pathlen)
            return
        
        next_r = ((r + new_d[1])+row) % row
        next_c = ((c + new_d[0])+col) % col
        go(next_r, next_c, di, start, pathlen+1)

    for r in range(row):
        for c in range(col):
            for di in range(len(directions)):
                d_str = "".join(map(str,directions[di]))
                if d_str in d_record[r][c]:
                    continue
                start = [r,c,directions[di]]
                next_r = ((r + directions[di][1])+row) % row
                next_c = ((c + directions[di][0])+col) % col
                go(next_r, next_c, di, start, pathlen)
    path_lens.sort()
    return path_lens