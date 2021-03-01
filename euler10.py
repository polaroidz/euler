def gen_primes():
    D = {}    

    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

s = 0
g = gen_primes()
p = next(g)

while p < 2*(10**6):
  p = next(g)
  s += p

print(s)
