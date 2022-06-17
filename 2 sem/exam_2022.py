def task_1(spisok, symbol):
    new_spisok = []
    for i in spisok:
        new_spisok.append(symbol * i)
    return new_spisok

print(f'Задание 1: {task_1([2, 3, 1], "x")}')


def task_2(spisok_1, spisok_2):
    stroka = ''
    for i in range(len(spisok_1)):
        stroka += spisok_1[i]
        if i == len(spisok_2):
            break
        else:
            stroka += spisok_2[i]
    return stroka

print(f'Задание 2: {task_2(["abc", "xyz", "pqrst"], ["##", "000"])}')


def task_3(spisok, number):
    new_spisok = []
    for i in range(number):
        new_spisok.append(spisok[i] + 1)
    for elem in spisok[number:]:
        new_spisok.append(elem)
    return new_spisok

print(f'Задание 3: {task_3([10, 20, 30, 40], 3)}')

spisok = [10, 20, 30, 40, 50]
def task_4(spisok, number):
    for i in range(number):
        spisok[i] += 1

task_4(spisok, 3)
print(f'Задание 4: {spisok}')

def task_5(L, n):
    c = L // n
    spisok = [c for i in range(n)]
    o = L % n
    for i in range(o):
        spisok[i] += 1
    return spisok

print(f'Задание 5: {task_5(20, 6)}')

def task_6(spisok, number):
    length = 0
    for word in spisok:
        length += len(word)
    len_space = number - length
    space = task_5(len_space, len(spisok) - 1)
    spaces = task_1(space, ' ')
    final_stroka = task_2(spisok, spaces)
    return final_stroka

print(f'Задание 6: {task_6(["one", "two", "three"], 18)}')

def task_7(spisok):
    stroka = ' '.join(spisok)
    return len(stroka)

print(f'Задание 7: {task_7(["abc", "xyz", "qqqqq"])}')

def task_8(file):
    with open(file, mode = 'r', encoding='utf-8') as f:
        text = f.read()
        l = len(text)
        word_list = text.split()
        l_words = len(word_list)
        space_text = task_7(word_list)
    return l, l_words, space_text

print(f'Задание 8: {task_8("file_8")}')