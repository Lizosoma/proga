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
            x = -c / b
        return f'одно решение x = {x:.2f}'
            elif b != 0:
                return f'одно решение x = {0 / b:.2f}'
            elif a != 0:
                return f'одно решение x = {0 / a:.2f}'
            elif a != 0 and c != 0:
                if -c / a > 0:
            x = (-c / a) ** 0.5
                    return f'два решения x1 = -{x:.2f}, x2 = {x:.2f}'    
                elif -c / a < 0:
                    return 'решений нет'
            elif a != 0 and b != 0:
                1 = 0 / a
                x2 = -b / a
                return f'два решения x1 = {min(x1, x2):.2f}, x2 = {max(x1, x2):.2f}'
    if D < 0:
        return 'решений нет'
    if D == 0:
        x = - b / (2 * a)
        return f'одно решение x = {x:.2f}'
    if D > 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        return f'два решения x1 = {min(x1, x2):.2f}, x2 = {max(x1, x2):.2f}'
print(roots(-10, -10, -2))

test(roots, 'quadratic_equation.json')
