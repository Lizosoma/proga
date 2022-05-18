def fib():
    a_prev, a = 0, 1
    while True:
        yield a
        a_prev, a = a, a + a_prev


fib = fib()
while True:
    print(next(fib))


def file_symbols(file):
    with open(file, mode="r", encoding="utf8") as f:

        file = f.readlines()
        for word in file:
            for symbol in word:
                yield symbol


print(list(file_symbols('some_file.txt')))


from split_words_gen import split_words_gen


def file_words(file):
    with open(file, mode="r", encoding="utf8") as g:
        file = split_words_gen(' '.join(g.readlines()))

        for word in file:
            yield word


print(list(file_words('some_file.txt')))


def zip(enum_1, enum_2):
    for i in range(len(enum_1)):
        yield (enum_1[i], enum_2[i])


print(list(zip([10, 20, 30], "abc")))


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
