from itertools import combinations

def is_palindrome(n):
  s = str(n)
  r = s[::-1]
  return s == r

a = range(100, 999)
a = combinations(a, 2)
a = map(lambda e: e[0] * e[1], a)
a = filter(is_palindrome, a)
a = max(a)

print(a)
