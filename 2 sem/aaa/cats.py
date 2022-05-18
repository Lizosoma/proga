def g(file):

    with open(file, mode="w", encoding="utf8") as f:

        for x in range(1, 1000):
            a = x % 100
            b = a // 10
                
            if x % 10 == 1 and x % 100 != 11:
                f.write (f'{x} кот\n')

            elif (x % 10 == 2 or x % 10 == 3 or x % 10 == 4) and b != 1:
                f.write (f'{x} кота\n')
                    
            else:
                f.write (f'{x} котов\n')

g(file = 'cats.txt')
