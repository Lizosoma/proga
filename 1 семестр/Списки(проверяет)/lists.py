from testsystem import test

def even_list(n):

    l = []
    for i in range(2, n * 2 + 1):
        if i % 2 == 0:
            l.append(i)
    return l
    
test(even_list, 'even_list.json.gz')

#=====

def list_of_empty_lists(n):

    l = [[] for i in range(n)]
    return l

test(list_of_empty_lists, 'list_of_empty_lists.json.gz')

#=====

def list_exchange_pure(a):

    l = a
    lNew = [i for i in l]
    lNew[0], lNew[-1] = lNew[-1], lNew[0]
    return lNew

test(list_exchange_pure, 'list_exchange_pure.json.gz')

#=====

def list_exchange_inplace(a):

    l = a
    l[0], l[-1] = l[-1], l[0]

test(list_exchange_inplace, 'list_exchange_inplace.json.gz')

#=====

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

#=====

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
