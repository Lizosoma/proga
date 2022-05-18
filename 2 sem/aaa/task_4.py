def g(file):

    with open(file, mode="r", encoding="utf8") as f:

        k = 0
        alphabet = 'йцукенгшщзхъфывапролджэёячсмитьбю'
        text = f.read()
        for letter in text:
            if letter.lower() in alphabet:
                k += 1

    return k

print(g('cats_2'))
