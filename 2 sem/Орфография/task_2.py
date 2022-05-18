from task_1 import task_1
from split_words_orph import split_words_orph


def task_2(words, text):
    with open(words, mode="r", encoding="utf8") as f, open(text, mode="r", encoding="utf8") as g:

        iskl = []
        mnozh_of_words = task_1(words)
        spisok_of_words = split_words_orph(g.read())

        for word_from_spisok in spisok_of_words:
            if word_from_spisok.lower() not in mnozh_of_words:
                iskl.append(word_from_spisok)

    return iskl


if __name__ == '__main__':
    print(task_2('words_alpha.txt', 'eng_text.txt'))
