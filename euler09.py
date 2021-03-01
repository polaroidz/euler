def is_triplet(t):
  a, b, c = t
  if not a < b < c:
    return False 

  return a**2 + b**2 == c**2 and a + b + c == 1000

from itertools import combinations

a = combinations(range(200, 500), 3)
a = filter(is_triplet, a)
a = next(a)

print(a, sum(a))
