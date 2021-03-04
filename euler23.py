import numpy as np
import sympy as sy

d = lambda n: sum(sy.divisors(n, proper=True))

a = range(12, 28123)
a = filter(lambda n: d(n) > n, a)
a = list(a)

S = []
end = len(a) - 1

for i in range(0, end):
  for j in range(i, end):
    n = a[i] + a[j]
    if n < 28123:
      S.append(n)

S = set(S)

s = 0

for i in range(1, 28123):
  if i not in S:
    s += i

s
