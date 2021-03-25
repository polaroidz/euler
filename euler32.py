def is_pandigital(n):
  s = str(n)

  return '0' not in s and len(s) == len(set(s))

l = []

for a in range(2, 9):
  b = range(1234, (10**4 - 1) // a)
  b = filter(is_pandigital, b)
  b = map(lambda n: (a, n, a * n), b)
  b = map(lambda t: (t[2], "".join([str(e) for e in t])), b)
  b = filter(lambda t: is_pandigital(t[1]), b)
  b = map(lambda t: t[0], b)
  b = list(b)

  l += b

for a in range(12, 98):
  b = range(123, (10**4 - 1) // a)
  b = filter(is_pandigital, b)
  b = map(lambda n: (a, n, a * n), b)
  b = map(lambda t: (t[2], "".join([str(e) for e in t])), b)
  b = filter(lambda t: is_pandigital(t[1]), b)
  b = map(lambda t: t[0], b)
  b = list(b)

  l += b

sum(set(l))
