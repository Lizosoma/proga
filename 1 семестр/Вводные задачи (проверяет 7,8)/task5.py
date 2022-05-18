from testsystem import test

def f(x):

    a = x % 100
    b = a // 10
    
    if x % 10 == 1 and x % 100 != 11:
        return (f'{x} кот')

    if (x % 10 == 2 or x % 10 == 3 or x % 10 == 4) and b != 1:
        return (f'{x} кота')

    else:
        return (f'{x} котов')

print(f(10))

test(f, 'cats.json')
