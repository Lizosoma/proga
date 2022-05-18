from testsystem import test
def f(x):

    a = x % 10
    b = x % 100
    c = b // 10

    if a == c:
        return True
    else:
        return False

print(f(455))

test(f, 'last_digits_are_similar.json')
