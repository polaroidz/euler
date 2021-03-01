import sympy as sy

def gen_triangular():
  a = 1
  
  while True:
    yield sum(range(a+1))
    a += 1

g = gen_triangular()
a = next(g)

while sy.divisor_count(a) < 500:
  a = next(g)

print(a)
