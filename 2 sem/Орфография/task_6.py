def task_6(another_word):

    mnozh = set()
    
    for index in range(len(another_word))[:-1]:
        slice_1 = another_word[:index]
        slice_2 = another_word[index:index + 2]
        slice_3 = another_word[index + 2:]
        word = slice_1 + slice_2[1] + slice_2[0] + slice_3
        mnozh.add(word)

    return mnozh

if __name__ == '__main__':
    print(task_6('hello'))