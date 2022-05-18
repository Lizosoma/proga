from split_words_orph import split_words_orph

def task_1(file):

    with open(file, mode="r", encoding="utf8") as f:

        mnozh_words = set(split_words_orph(f.read()))

    return mnozh_words

if __name__ == '__main__':
    print(task_1('words_alpha.txt'))
