def eat(*args):
    numbers = args
    for num in numbers:
        if num % 2 == 0:
            print('Ok')
            return
    print('I like evens')


eat(3, 79, 35, 657)