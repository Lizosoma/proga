from testsystem import test

def get_equation(a, b, c):

    equation = ''

    if a != 0:
        if a == 1:
            equation += 'x^2'
        elif a == -1:
            equation += '-x^2'
        else:
            equation += f'{a}x^2'
        if b != 0:
            if b > 0:
                if b == 1:
                    equation += '+x'
                else:
                    equation += f'+{b}x'
            else:
                if b == -1:
                    equation += '-x'
                else:
                    equation += f'{b}x'
        if c != 0:
            if c > 0:
                equation += f'+{c}'
            else:
                equation += f'{c}'
    else:
        if b != 0:
            if b > 0:
                if b == 1:
                    equation += 'x'
                else:
                    equation += f'{b}x'
            else:
                if b == -1:
                    equation += '-x'
                else:
                    equation += f'{b}x'
        if c != 0:
            if c > 0:
                equation += f'+{c}'
            else:
                equation += f'{c}'

    if 'x' in equation:
        return equation
    elif '+' in equation:
        return equation.removeprefix('+')
    elif equation == '':
        return '0'
    else:
        return equation

test(get_equation, "poly.json.gz")

def get_text(num):
    units = {1: ' один ', 2: ' два ', 3: ' три ', 4: ' четыре ', 5: ' пять ', 6: ' шесть ', 7: ' семь ', 8: ' восемь ',
             9: ' девять ', 0: 'ноль'}
    units_fe = {1: ' одна ', 2: ' две ', 3: ' три ', 4: ' четыре ', 5: ' пять ', 6: ' шесть ', 7: ' семь ',
                8: ' восемь ', 9: ' девять '}
    dozens = {1: ' десять ', 2: ' двадцать ', 3: ' тридцать ', 4: ' сорок ', 5: ' пятьдесят ', 6: ' шестьдесят ',
              7: ' семьдесят ', 8: ' восемьдесят ', 9: ' девяносто '}
    dozens_bf20 = {1: ' одиннадцать ', 2: ' двенадцать ', 3: ' тринадцать ', 4: ' четырнадцать ', 5: ' пятнадцать ',
                   6: ' шестнадцать ', 7: ' семнадцать ', 8: ' восемнадцать ', 9: ' девятнадцать '}
    hundreds = {1: ' сто ', 2: ' двести ', 3: ' триста ', 4: ' четыреста ', 5: ' пятьсот ', 6: ' шестьсот ',
                7: ' семьсот ',
                8: ' восемьсот ', 9: ' девятьсот '}

    number = []
    triple = 0
    prev_digit = 0
    num = str(num)

    for position, digit in enumerate(num[::-1]):
        digit = int(digit)
        if position % 3 == 0:
            triple += 1
            if triple == 2:
                if len(num) > 4 and int(num[-position-2]) == 1 and digit != 0:
                    number.append(f' {dozens_bf20[digit]} тысяч ')
                    prev_digit = 10
                else:
                    if digit == 1:
                        number.append(f' {units_fe[digit]} тысяча ')
                    elif digit in range(2, 5):
                        number.append(f' {units_fe[digit]} тысячи ')
                    elif digit in range(5, 10):
                        number.append(f' {units_fe[digit]} тысяч ')
                    elif len(set(num[-4:-7:-1])) != 1 and len(num) > 4:
                        number.append(' тысяч ')
                    prev_digit = digit

            elif triple == 3:
                if len(num) > 7 and int(num[-position-2]) == 1 and digit != 0:
                    number.append(f' {dozens_bf20[digit]} миллионов ')
                    prev_digit = 10
                else:
                    if digit == 1:
                        number.append(f' {units[digit]} миллион ')
                    elif digit in range(2, 5):
                        number.append(f' {units[digit]} миллиона ')
                    elif digit in range(5, 10):
                        number.append(f' {units[digit]} миллионов ')
                    else:
                        number.append(' миллионов ')
                    prev_digit = digit
            else:
                prev_digit = digit
                if len(num) == 1:
                    number.append(units[digit])
        elif position % 3 == 1 and prev_digit != 10:
            if digit == 1:
                if prev_digit != 0:
                    number.append(dozens_bf20[prev_digit])
                else:
                    number.append(dozens[digit])
            elif digit != 0:
                if prev_digit != 0 and triple == 1:
                    number.append(units[prev_digit])
                number.append(dozens[digit])
            elif triple == 1:
                if prev_digit != 0:
                    number.append(units[prev_digit])
            prev_digit = digit
        elif position % 3 == 2:
            if digit != 0:
                number.append(hundreds[digit])
            prev_digit = digit

    g = ''
    for word in number[::-1]:
        g += word
    g = ' '.join(g.split())

    return g

print(get_text(110000000))

test(get_text, "number_to_string.json.gz")
