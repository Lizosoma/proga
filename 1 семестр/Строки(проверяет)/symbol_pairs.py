from testsystem import test

def symbol_pairs(word):

    s = '' 
    s += str(word) 
    sch = s[1::2]
    snch = s[::2]
    if sch == snch:
        return True
    else:
        return False

test(symbol_pairs, 'symbol_pairs.json.gz')


