from testsystem import test

def square(n):
    
    s = ''
    for i in range(n):
        s += 'x' * n
        s += '\n'
    return s

print(square(5))

test(square, 'square.json')
