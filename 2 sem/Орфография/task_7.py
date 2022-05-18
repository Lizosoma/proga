from task_4 import task_4
from task_5 import task_5
from task_6 import task_6

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

if __name__ == '__main__':
    print(task_7('act', 'words_alpha.txt'))