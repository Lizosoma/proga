def one_two_two():
    k = 1
    while True:
        for i in range(k):
            yield k
        k += 1


def func(n):
    l = []
    one_two_two_ = one_two_two()
    for i in range(n):
        l.append(int(next(one_two_two_)))
    return l


print(func(10))
