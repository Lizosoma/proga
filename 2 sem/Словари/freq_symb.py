def freq_symb(string):

    vocabulary = {}
    for letter in string:
        if letter not in vocabulary:
            vocabulary[letter] = 1
        else:
            vocabulary[letter] += 1

    return vocabulary

if __name__ == '__main__':
    print(freq_symb('banana'))
