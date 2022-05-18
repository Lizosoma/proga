from freq_words import freq_words

def csv(read_text, written_text):

    with open(read_text, mode="r", encoding="utf8") as f, open(written_text, mode="w", encoding="cp1251") as g:

        text_1 = f.read().lower()
        voc = freq_words(text_1)
        for word in voc.keys():
            g.write(f'{word};{voc[word]}\n')

print(csv('read_text', 'written_text'))