from task_1 import task_1
from task_7 import task_7
from split_words_orph import split_words_orph


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
