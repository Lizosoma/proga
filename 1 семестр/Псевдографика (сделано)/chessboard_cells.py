from testsystem import test

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
