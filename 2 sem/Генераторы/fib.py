def fib():
    a_prev, a = 0, 1
    while True:
        yield a
        a_prev, a = a, a + a_prev


fib = fib()
while True:
    print(next(fib))
