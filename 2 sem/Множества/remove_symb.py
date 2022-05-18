def remove_symb(line, mnozh):

    spisok = []
    for i in line:
        if i not in mnozh:
            spisok.append(i)

    stroka = ''.join(spisok)

    return stroka

print(remove_symb('pigeon says kurlyk-kurlyk', {'k', 'y'}))