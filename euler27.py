n = 1
s = 1
i = 0
d = 1

while d < 1001:
  r = 2 + i*2
  for _ in range(0, 4):
    n += r
    s += n
  i += 1
  d += 2

s
