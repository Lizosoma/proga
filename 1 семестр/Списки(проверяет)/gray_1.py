from testsystem import test

def gray_1(n):

    l = [0]
    if n == 0:
        return l
    
    else:
        for a in range(n):
            l1 = l + [a+1] + l
            l = [x for x in l1]
        return l1

test(gray_1, 'gray_1.json')
