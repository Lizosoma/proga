from testsystem import test

def roots(a, b, c):

    D = b ** 2 - 4 * a * c

    if a == 0:
        if b == 0:
            if c == 0:
                return 'решений бесконечно много'
            else:
                return 'решений нет'
        else:
            return f'одно решение x = {-c / b:.2f}'
    elif D < 0:
        return 'решений нет'
    elif D == 0:
        return f'одно решение x = {-b / (2 * a):.2f}'
    elif D > 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        f'два решения x1 = {min(x1, x2):.2f}, x2 = {max(x1, x2):.2f}'
    else:
        'решений нет'

    
print(roots(-10, -10, -2))

test(roots, 'quadratic_equation.json')
