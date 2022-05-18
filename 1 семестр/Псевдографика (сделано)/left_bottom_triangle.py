from testsystem import test

def triangle(n):

    s = ''
    for a in range(n):
        s += 'x' * (a+1) + '\n'
    return s

print(triangle(5))

test(triangle, 'left_bottom_triangle.json')
