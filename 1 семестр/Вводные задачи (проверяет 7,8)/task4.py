from testsystem import test

def f(x):

    if x % 4 != 0:
        return False

    elif x % 100 != 0:
        return True
    
    elif x % 100 == 0 and x % 400 == 0:
        return True

    else:
        return False

print(f(2021))

test(f, 'is_leap.json')
