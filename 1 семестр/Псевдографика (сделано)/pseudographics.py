from testsystem import test

def square(n):
    
    s = ''
    for i in range(n):
        s += 'x' * n
        s += '\n'
    return s

print(square(5))

test(square, 'square.json')


def triangle(n):

    s = ''
    for a in range(n):
        s += 'x' * (a+1) + '\n'
    return s

print(triangle(5))

test(triangle, 'left_bottom_triangle.json')


def triangle_2(n):

   s = ''
   for i in range(n, 0, -1):
      s += 'x' * i + '\n'
   return s

print(triangle_2(5))

test(triangle_2, 'left_up_triangle.json')


def triangle_3(n):

    s = ''
    for i in range (n):
        l = 'x' * (i + 1)
        l = l.rjust(n)
        s += l + '\n'
    return s

print(triangle_3(5))

test(triangle_3, 'right_bottom_triangle.json')


def chessboard(n):
    
    s = ''
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                s += '1'
            else:
                s += '0'
        s += '\n'
    return s

print(chessboard(5))

test(chessboard, 'chessboard.json')


def chessboard_cells(n, k):

    l = ''
    for i in range(n):
        s = ''
        for j in range(n):
            if (i + j) % 2 == 0:
                s += '1' * k
            else:
                s += '0' * k
        for j in range(k):
            l += s + '\n'
    return l

print(chessboard_cells(2, 3))

test(chessboard_cells, 'chessboard_cells.json')


def table(m, n):
    
    s = ''
    
    a = '\u250C'
    b = '\u2500\u252C'
    c = '\u2500\u2510\n'
    d = '\u2502 '
    d1 = '\u2502\n'
    e = '\u251C'
    f = '\u2500\u253C'
    g = '\u2500\u2524\n'
    h = '\u2514'
    i = '\u2500\u2534'
    j = '\u2500\u2518'
    
    line = a + b * (n - 1) + c
    line2 = d * n + d1
    line3 = e + f * (n - 1) + g
    line4 = h + i * (n - 1) + j

    s = line + (line2 + line3) * (m - 1) + line2 + line4 + '\n'
    return s

print(table(5, 8))

test(table, 'table.json')
