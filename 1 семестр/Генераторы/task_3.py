def gen(n):

    l = [int(x) for x in n if x.isdigit()]

    return l

print(gen(['1', 'a', '42']))
