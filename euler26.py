def mul_order(a, n): 
    if (gcd(a, n) != 1): 
        return -1
    result = 1
    k = 1
    while (k < n) : 
        result = (result * a) % n
        if (result == 1) : 
            return k 
        k = k + 1
    return -1

a = range(2, 1000)
a = map(lambda n: (n, mul_order(10, n)), a)
a = max(a, key=lambda e: e[1])

a
