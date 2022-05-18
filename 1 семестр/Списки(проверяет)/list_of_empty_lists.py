from testsystem import test

def list_of_empty_lists(n):

    l = [[] for i in range(n)]
    return l

test(list_of_empty_lists, 'list_of_empty_lists.json.gz')
