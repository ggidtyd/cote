def solution(n):
    tiles = [0] * 5001

    mod = 1000000007
    tiles[0] = 1
    tiles[2] = 3
    
    for i in range(4, n+1, 2):
        tiles[i] = (tiles[i-2]*4 % mod - tiles[i-4] % mod + mod) % mod

    return tiles[n]