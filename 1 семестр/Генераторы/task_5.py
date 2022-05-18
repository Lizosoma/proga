def gen(n):

    ints = list(range(2, n))
    primes = []
    while len(ints) != 0:
        p = ints[0]
        primes.append(p)
        ints = [x for x in ints if x % p != 0]

    return primes

print(gen(15))
