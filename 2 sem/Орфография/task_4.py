def task_4(some_word):

    mnozh_of_words = set()

    for number_letter in range(len(some_word)):

        mnozh_of_words.add(some_word[:number_letter] + some_word[number_letter + 1:])

    return mnozh_of_words

if __name__ == '__main__':
    print(task_4('ccat'))
