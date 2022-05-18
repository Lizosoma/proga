from split_words_voc import split_words_voc


def sub(vocabulary, string):

    voc = str.maketrans(vocabulary)
    new_string = string.translate(voc)
    return new_string

print(sub({'a': 'xyz', 'b': '123'}, 'abc'))


def freq_symb(string):

    vocabulary = {}
    for letter in string:
        if letter not in vocabulary:
            vocabulary[letter] = 1
        else:
            vocabulary[letter] += 1

    return vocabulary

print(freq_symb('banana'))


def freq_words(text):

    vocabulary = {}
    text = split_words_voc(text)
    vocabulary = freq_symb(text)

    return vocabulary

print(freq_words('Вживую шелкопряды вряд ли покажутся столь милыми широкой публике, но тут о них говорят с исключительной любовью. Их время — весна, когда сохраняется идеальная для этих насекомых температура воздуха примерно в 25 градусов.'))


def csv(read_text, written_text):

    with open(read_text, mode="r", encoding="utf8") as f, open(written_text, mode="w", encoding="cp1251") as g:

        text_1 = f.read().lower()
        voc = freq_words(text_1)
        for word in voc.keys():
            g.write(f'{word};{voc[word]}\n')

print(csv('read_text', 'written_text'))