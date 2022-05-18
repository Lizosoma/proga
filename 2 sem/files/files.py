print('Задание 1')

def z_1():
    with open('text.txt', mode='r', encoding='utf8') as f:

        words = []
        symbols = 0
        lines = f.readlines()
        count_lines = len(lines)

        for line in lines:
            words += line.split()
        count_words = len(words)

        for word in words:
            symbols += len(word)
        avg_symbols = round(symbols / len(words), 2)

    return f'количество строк: {count_lines}\nколичество слов: {count_words}\nсредняя длина слова: {avg_symbols}'


print(z_1())

print('\nЗадание 2')

def z_2():

    with open('text.txt', encoding = 'utf8') as f, open('text.txt', encoding = 'utf8') as g:

        text_1 = f.read().split()

        line = []
        text_2 = g.readlines()
        for lines in text_2:
            line.append(lines.split())

    return f'{text_1},\n{line}'


print(z_2())

print('\nЗадание 3')

def z_3():

    with open('text.txt', mode='rb') as f:

        bities = {}
        bities_sorted = []

        text = f.read().split()
        for word in text:
            array = bytearray(word)
            for byte in array:
                if byte in bities:
                    bities[byte] += 1
                else:
                    bities[byte] = 1

        for pair in bities.items():
            a, b = pair
            bities_sorted.append([b, a])
            bities_sorted.sort()
        return max(bities_sorted)[1]

print(z_3())

print('\nЗадание 4')

def z_4(read_file, write_file):

    with open(read_file, mode='r', encoding='utf8') as f:

        text = f.read()
        new_str = ''

        for symbol in text:
            new_str += symbol * 2

        with open(write_file, mode='w', encoding='utf8') as g:

            g.write(new_str)

z_4('text.txt', 'new_text.txt')