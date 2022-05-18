from testsystem import test

def list_exchange_pure(a):

    l = a
    lNew = [i for i in l]
    lNew[0], lNew[-1] = lNew[-1], lNew[0]
    return lNew

test(list_exchange_pure, 'list_exchange_pure.json.gz')
