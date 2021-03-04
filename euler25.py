import sympy as sy

idx = 10**3

while True:
  a = sy.fibonacci(idx)
  a = str(a)

  if len(a) >= 1000:
    break
  
  idx += 1

a, idx
