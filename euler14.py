import numpy as np
from sympy.ntheory.generate import primerange

def collatz_count(n, count=1):
  if n in p2:
    return count + p2[n]
  if n % 2 == 0:
    return collatz_count(n / 2, count + 1)
  else:
    return collatz_count(3*n + 1, count + 1)

p2 = range(20)
p2 = map(lambda e: (2**(e+1), e + 1), p2)
p2 = dict(p2)

for p in primerange(1, 10**6):
  count = collatz_count(p)
  p2[p] = count

m, c = 1, 0

for i in range(1, 10**6, 2):
  count = collatz_count(i)
  if count > c:
    m = i
    c = count

print(m)
