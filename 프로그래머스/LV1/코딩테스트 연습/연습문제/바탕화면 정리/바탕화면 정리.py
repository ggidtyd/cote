def solution(wallpaper):
    lux, luy, rdx, rdy = 51, 51, -1, -1
    R, C = len(wallpaper), len(wallpaper[0])
    for r in range(R):
        for c in range(C):
            if wallpaper[r][c] == '#':
                lux = min(lux, r)
                luy = min(luy, c)
                rdx = max(rdx, r+1)
                rdy = max(rdy, c+1)
    return [lux, luy, rdx, rdy]