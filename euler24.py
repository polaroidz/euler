from itertools import permutations

a = permutations(range(0, 10))
a = list(a)
a[10**6 - 1]
