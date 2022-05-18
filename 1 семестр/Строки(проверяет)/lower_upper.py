from testsystem import test

def lower_upper(word):

    s = ''
    s += str(word)
    s1 = s[::2]
    s2 = s[1::2]
    if (s1.islower() and s2.isupper()) or (s1.isupper() and s2.islower()):
        return True
    else:
        return False

print(l_u('FhYoBrF'))

test(lower_upper, 'lower_upper.json.gz')
