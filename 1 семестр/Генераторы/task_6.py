def gen(n):

    ns = {x for x in range(1, int(n ** 0.5) + 1) if n%x == 0}
    ns1 = {n // x for x in range(1, int(n ** 0.5) + 1) if n%x == 0}
    ns_new = ns & ns1

    return ns_new

print(gen(555))
