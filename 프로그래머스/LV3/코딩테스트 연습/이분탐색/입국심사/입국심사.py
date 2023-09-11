from itertools import permutations, combinations
s = [1, 2, 3, 4, 5]

result = combinations(s, len(s))

for arr in result:
    print(arr)