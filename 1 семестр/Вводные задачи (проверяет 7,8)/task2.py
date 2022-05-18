from testsystem import test

def f(x):
    
    if x % 10 == 5:
        return True
    
    else:
        return False

print(f(75))

test(f, 'last_is_5.json')
