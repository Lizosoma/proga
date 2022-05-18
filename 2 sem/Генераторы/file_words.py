from split_words_gen import split_words_gen


def file_words(file):
    with open(file, mode="r", encoding="utf8") as g:
        file = split_words_gen(' '.join(g.readlines()))

        for word in file:
            yield word


print(list(file_words('some_file.txt')))
