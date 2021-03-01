import math

def is_prime(n):
    if n < 2:
        return False

    if n % 2 == 0:
        return n == 2

    for i in range(3, n, 2): 
        if n % i == 0:
            return False

    return True
  
n = 1
a = 1

while n < 10001:
  a += 2

  if is_prime(a):
    n += 1

a, is_prime(a)
