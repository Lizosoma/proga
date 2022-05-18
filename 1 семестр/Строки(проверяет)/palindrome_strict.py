from testsystem import test

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
