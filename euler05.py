def is_divisible(n):
  for i in range(2, 20):
    if n % i != 0:
      return False
  return True

a = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19

a * 24, is_divisible(a * 24)

# 24 because when its the smallest divisor of the non-primes
# factors of 20!
