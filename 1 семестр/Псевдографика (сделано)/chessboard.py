from testsystem import test

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
