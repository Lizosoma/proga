from testsystem import test

def list_exchange_inplace(a):

    l = a
    l[0], l[-1] = l[-1], l[0]

test(list_exchange_inplace, 'list_exchange_inplace.json.gz')
