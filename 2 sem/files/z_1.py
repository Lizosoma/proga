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
