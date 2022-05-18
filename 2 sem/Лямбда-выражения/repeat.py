def repeat(**kwargs):
    words = kwargs
    spisok = []
    for word in words:
        for i in range(words[word]):
            spisok.append(word)
    return spisok


print(repeat(hello=2, cat=3))