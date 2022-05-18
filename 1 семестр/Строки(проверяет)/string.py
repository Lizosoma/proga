from testsystem import test

def palindrome(word):
    
    s = ''
    s += str(word)
    if s == s[::-1]:
        return True
    else:
        return False

test(palindrome, 'palindrome.json.gz')

#=====

def palindrome_strict(word, strict):
    
    s = ''
    s += str(word)
    if not strict:
        spaces = s.split()
        new_s = ''.join(spaces)
        new_s = new_s.lower()
        if new_s == new_s[::-1]:
            return True
        else:
            return False
    else:
        if s == s[::-1]:
            return True
        else:
            return False

test(palindrome_strict, 'palindrome_strict.json.gz')

#=====

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

#=====

def lower_upper(word):

    s = ''
    s += str(word)
    s1 = s[::2]
    s2 = s[1::2]
    if (s1.islower() and s2.isupper()) or (s1.isupper() and s2.islower()):
        return True
    else:
        return False

test(lower_upper, 'lower_upper.json.gz')

#=====

def exchange_01(word):

    s = '' + str(word)
    rules = str.maketrans('10', '01')
    return s.translate(rules)

test(exchange_01, 'exchange_01.json.gz')

#=====

def exchange_symbols(word, char1, char2):

    s = '' + str(word)
    rules = str.maketrans(char1 + char2, char2 + char1)
    return s.translate(rules)

test(exchange_symbols, 'exchange_symbols.json.gz')

#=====

def dragon_curve(n):

    S = 'R'
    rules = str.maketrans('RL', 'LR')
    
    if n == 0:
        return S
    
    else:
        for S1 in range(n):
            S1 = S + 'R' + S[::-1].translate(rules)
            S = S1
        return S1

test(dragon_curve, 'dragon_curve.json.gz')
