from testsystem import test

def task1(x):

    k = 0
    while x > 0:
        x //= 10
        k += 1

    if k == 3:
        return True

    else:
        return False

print(task1(10000))

test(task1, "has_3_digits.json")
