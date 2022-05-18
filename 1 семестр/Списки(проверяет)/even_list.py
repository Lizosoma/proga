from testsystem import test

def even_list(n):

    l = []
    for i in range(2, n * 2 + 1):
        if i % 2 == 0:
            l.append(i)
    return l
    
test(even_list, 'even_list.json.gz')
