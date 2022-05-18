from testsystem import test

def palindrome(word):
    
    s = ''
    s += str(word)
    if s == s[::-1]:
        return True
    else:
        return False

test(palindrome, 'palindrome.json.gz')
