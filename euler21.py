import sympy as sy

d = lambda n: sum(sy.divisors(n, proper=True))

def is_amicable(a):
  b = d(a)
  if a == b:
    return False
  return d(b) == a

a = range(1, 10000)
a = filter(is_amicable, a)
a = list(a)

sum(a)
