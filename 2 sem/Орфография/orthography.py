from split_words_orph import split_words_orph
import string


def task_1(file):

    with open(file, mode="r", encoding="utf8") as f:

        return set(split_words_orph(f.read()))


print(f'Задание 1:\n{task_1("words_alpha.txt")}\n')


def task_2(words, text):
    with open(text, mode="r", encoding="utf8") as g:

        iskl = []
        mnozh_of_words = task_1(words)
        spisok_of_words = split_words_orph(g.read())

        for word_from_spisok in spisok_of_words:
            if word_from_spisok.lower() not in mnozh_of_words:
                iskl.append(word_from_spisok)

    return iskl

print(f'Задание 2:\n{task_2("words_alpha.txt", "eng_text.txt")}\n')


def task_3(wr_text):

    with open(wr_text, mode="w", encoding="utf8") as w:

        w.write(str(task_2('words_alpha.txt', 'eng_text.txt')))

print(f'Задание 3:\n{task_2("words_alpha.txt", "eng_text.txt")}\n')
task_3(wr_text='written_text')


def task_4(some_word):

    mnozh_of_words = set()

    for number_letter in range(len(some_word)):

        mnozh_of_words.add(some_word[:number_letter] + some_word[number_letter + 1:])

    return mnozh_of_words

print(f'Задание 4:\n{task_4("ccat")}\n')


def task_5(other_word):

    mnozh_of_new_words = set()
    const = string.ascii_lowercase

    for num_of_letter in range(len(other_word) + 1):
        for letter in const:

            mnozh_of_new_words.add(other_word[:num_of_letter] + letter + other_word[num_of_letter:])

    return mnozh_of_new_words

print(f"Задание 5:\n{task_5('at')}\n")


def task_6(another_word):
    mnozh = set()

    for index in range(len(another_word))[:-1]:
        slice_1 = another_word[:index]
        slice_2 = another_word[index:index + 2]
        slice_3 = another_word[index + 2:]
        word = slice_1 + slice_2[1] + slice_2[0] + slice_3
        mnozh.add(word)

    return mnozh

print(f"Задание 6:\n{task_6('hello')}\n")


def task_7(word, dic):

    with open(dic, mode='r', encoding='utf8') as f:

        r = f.read()

        mnozh = set()

        words_4 = task_4(word)
        words_5 = task_5(word)
        words_6 = task_6(word)
        words = words_4 | words_5 | words_6

        for letter in words:
            if letter.lower() in r:
                mnozh.add(letter)

    return mnozh

print(f"Задание 7:\n{task_7('act', 'words_alpha.txt')}\n")


def task_8(words, text):
    with open(words, mode="r", encoding="utf8") as f, open(text, mode="r", encoding="utf8") as g:

        mnozh_of_words = task_1(words)
        spisok_of_words = split_words_orph(g.read())

        for word_from_spisok in spisok_of_words:
            if word_from_spisok.lower() not in mnozh_of_words:
                if task_7(word_from_spisok, words):
                    print(f'! {word_from_spisok}, возможные исправления: {task_7(word_from_spisok, words)}')
                else:
                    print(f'! {word_from_spisok}, возможные исправления: Исправлений нет')

            else:
                print(word_from_spisok)

task_8('words_alpha.txt', 'eng_text.txt')