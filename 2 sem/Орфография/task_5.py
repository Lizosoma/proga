import string

def task_5(other_word):

    mnozh_of_new_words = set()
    const = string.ascii_lowercase

    for num_of_letter in range(len(other_word) + 1):
        for letter in const:

            mnozh_of_new_words.add(other_word[:num_of_letter] + letter + other_word[num_of_letter:])

    return mnozh_of_new_words

if __name__ == '__main__':
    print(task_5('at'))