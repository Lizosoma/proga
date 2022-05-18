def z_2():

    with open('text.txt', encoding = 'utf8') as f, open('text.txt', encoding = 'utf8') as g:

        text_1 = f.read().split()

        line = []
        text_2 = g.readlines()
        for lines in text_2:
            line.append(lines.split())

    return f'{text_1},\n{line}'


print(z_2())
