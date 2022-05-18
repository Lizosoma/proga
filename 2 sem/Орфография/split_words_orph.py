import string

def split_words_orph(text):

    const = string.punctuation
    text = text.split()
    for i in range(len(text)):
        text[i] = text[i].strip(const)

    return text
