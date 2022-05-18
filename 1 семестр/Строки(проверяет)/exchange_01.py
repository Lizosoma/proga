from testsystem import test

def exchange_01(word):

    s = '' + str(word)
    rules = str.maketrans('10', '01')
    return s.translate(rules)

test(exchange_01, 'exchange_01.json.gz')
