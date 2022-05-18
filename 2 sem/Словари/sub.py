def sub(vocabulary, string):

    voc = str.maketrans(vocabulary)
    new_string = string.translate(voc)
    return new_string

print(sub({'a': 'xyz', 'b': '123'}, 'abc'))