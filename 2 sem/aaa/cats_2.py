def g(file):

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


g(file = 'cats_2')
