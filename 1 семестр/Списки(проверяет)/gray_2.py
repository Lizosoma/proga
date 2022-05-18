from testsystem import test
from gray_1 import gray_1

def gray_2(n):

    grays = []
    positions = gray_1(n - 1)
    gray = [0] * n
    grays.append([x for x in gray])
    for i in positions:
        if gray[i] == 0:
            gray[i] = 1
        else:
            gray[i] = 0
        temp = [x for x in gray]
        grays.append(temp)

    return grays

test(gray_2, 'gray_2.json')
