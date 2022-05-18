def graph(func, m=0, n=10):
    for i in range(m, n + 1):
        f = func(i)
        print(f'f({i}) = {f}')


def squaring(x):
    return x ** 2


g = lambda x: x ** 2

graph(g, 10, 33)
graph(squaring)
