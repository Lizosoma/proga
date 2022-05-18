from testsystem import test

def exchange_symbols(word, char1, char2):

    s = '' + str(word)
    rules = str.maketrans(char1 + char2, char2 + char1)
    return s.translate(rules)

test(exchange_symbols, 'exchange_symbols.json.gz')
