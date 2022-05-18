def gen(n):

    l = [x for x in n if x % 2 != 0]

    return l

print(gen([1, 2, 4, 6, 8, 123456, 33, 43, 43,  54]))
    
