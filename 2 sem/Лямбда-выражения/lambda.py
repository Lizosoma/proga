def graph(func, m=0, n=10):
    for i in range(m, n + 1):
        f = func(i)
        print(f'f({i}) = {f}')


def squaring(x):
    return x ** 2


g = lambda x: x ** 2

graph(g, 10, 33)
graph(squaring)


def eat(*args):
    numbers = args
    for num in numbers:
        if num % 2 == 0:
            print('Ok')
            return
    print('I like evens')


eat(3, 79, 35, 657)


def repeat(**kwargs):
    words = kwargs
    spisok = []
    for word in words:
        for i in range(words[word]):
            spisok.append(word)
    return spisok


print(repeat(hello=2, cat=3))