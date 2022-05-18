from testsystem import test

def triangle_3(n):

    s = ''
    for i in range (n):
        l = 'x' * (i + 1)
        l = l.rjust(n)
        s += l + '\n'
    return s

print(triangle_3(5))

test(triangle_3, 'right_bottom_triangle.json')
