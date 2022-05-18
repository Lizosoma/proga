def file_symbols(file):
    with open(file, mode="r", encoding="utf8") as f:

        file = f.readlines()
        for word in file:
            for symbol in word:
                yield symbol


print(list(file_symbols('some_file.txt')))
