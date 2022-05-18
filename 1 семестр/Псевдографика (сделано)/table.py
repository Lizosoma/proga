from testsystem import test
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
