print('Задание 1')

def g_1(file):
    with open(file, mode="w", encoding="utf8") as f:
        for x in range(1, 101):
            f.write(f'{x}\n')


g_1(file='1_to_100.txt')

print('Задание 2')

def g_2(file):
    with open(file, mode="w", encoding="utf8") as f:

        for x in range(1, 1000):
            a = x % 100
            b = a // 10

            if x % 10 == 1 and x % 100 != 11:
                f.write(f'{x} кот\n')

            elif (x % 10 == 2 or x % 10 == 3 or x % 10 == 4) and b != 1:
                f.write(f'{x} кота\n')

            else:
                f.write(f'{x} котов\n')


g_2(file='cats.txt')

print('Задание 3')

def g_3(file):

    with open(file, mode="w", encoding="utf8") as f:

        units = {0: '', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
        el_nine = {0: 'десять', 1: 'одиннадцать', 2: 'двенадцать', 3: 'тринадцать', 4: 'четырнадцать', 5: 'пятнадцать', 6: 'шестнадцать', 7: 'семнадцать', 8: 'восемнадцать', 9: 'девятнадцать'}
        tens = {0: '', 2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят', 6: 'шестьдесят', 7: 'семьдесят', 8: 'восемьдесят', 9: 'девяносто'}
        hundreds = {0: '', 1: 'сто', 2: 'двести', 3: 'триста', 4: 'четыреста', 5: 'пятьсот', 6: 'шестьсот', 7: 'семьсот', 8: 'восемьсот', 9: 'девятьсот'}

        for x in range(1, 1000):

            text_x = str(x)

            if len(text_x) == 3:
                hundred = int(text_x[0])
                ten = int(text_x[1])
                unit = int(text_x[2])

            elif len(text_x) == 2:
                hundred = 0
                ten = int(text_x[0])
                unit = int(text_x[1])

            elif len(text_x) == 1:
                hundred = 0
                ten = 0
                unit = int(text_x[0])

            if ten != 1:
                if unit == 1:
                    cats = f'{hundreds[hundred]} {tens[ten]} {units[unit]} кот'.split()
                    cats = ' '.join(cats) + '\n'
                    f.write(cats)
                elif unit in (2, 3, 4):
                    cats = f'{hundreds[hundred]} {tens[ten]} {units[unit]} кота'.split()
                    cats = ' '.join(cats) + '\n'
                    f.write(cats)
                else:
                    cats = f'{hundreds[hundred]} {tens[ten]} {units[unit]} котов'.split()
                    cats = ' '.join(cats) + '\n'
                    f.write(cats)
            else:
                cats = f'{hundreds[hundred]} {el_nine[unit]} котов'.split()
                cats = ' '.join(cats) + '\n'
                f.write(cats)


g_3(file = 'cats_2')

print('Задание 4')

def g_4(file):

    with open(file, mode="r", encoding="utf8") as f:

        k = 0
        alphabet = 'йцукенгшщзхъфывапролджэёячсмитьбю'
        text = f.read()
        for letter in text:
            if letter.lower() in alphabet:
                k += 1

    return k

print(g_4('cats_2'))
