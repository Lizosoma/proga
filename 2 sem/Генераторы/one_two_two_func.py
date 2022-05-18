def one_two_two_func_1(n):
    k = 1
    for i in range(n):
        yield str(k) * k
        k += 1


print(list(one_two_two_func_1(5)))


def one_two_two_func_2(n):
    k = 1
    while k <= n:
        yield str(k) * k
        k += 1


print(list(one_two_two_func_2(5)))
