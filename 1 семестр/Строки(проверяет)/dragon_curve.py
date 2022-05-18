from testsystem import test

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
print(dragon_curve(2))
test(dragon_curve, 'dragon_curve.json.gz')
