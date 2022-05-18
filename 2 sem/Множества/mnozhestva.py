def all_letters(x):

    x = set(x)

    return x

print(f'Задание 1: {all_letters("ppiiggeeoonn")}')


def remove_symb(line, mnozh):

    spisok = []
    for i in line:
        if i not in mnozh:
            spisok.append(i)

    stroka = ''.join(spisok)

    return stroka

print(f'Задание 2: {remove_symb("pigeon says kurlyk-kurlyk", {"k", "y"})}')


import string

def split_words(text):

    const = string.punctuation
    text = text.split()
    for i in range(len(text)):
        text[i] = text[i].strip(const)

    return text

print(f'Задание 3: {split_words("Вживую шелкопряды вряд ли покажутся столь милыми широкой публике, но тут о них говорят с исключительной любовью. Их время — весна, когда сохраняется идеальная для этих насекомых температура воздуха примерно в 25 градусов.")}')


def common_words(stroka_1, stroka_2):

    line_1 = set(split_words(stroka_1))
    line_2 = set(split_words(stroka_2))
    first_task = line_1 & line_2

    for word_1 in line_1:
        line_1.remove(word_1)
        word_1 = word_1.lower()
        line_1.add(word_1)

    for word_2 in line_2:
        line_2.remove(word_2)
        word_2 = word_2.lower()
        line_2.add(word_2)

    return f'Задание 4.1: {first_task}\nЗадание 4.2: {line_1 & line_2}'

print(common_words('Тутовые шелкопряды не кусаются, а заняты только поеданием листьев с перерывами на сон — в общем, ведут исключительно здоровый образ жизни. Чтобы они смогли закончить работу, нужно беречь их покой. «Если напугать шелкопряда, волокно порвется», — рассказывают в Музее шелка в Шэнцзе, символ которого — мультяшная гусеница с листиком на голове.', 'Тутовые шелкопряды вживую вряд ли покажутся столь милыми широкой публике, но тут о них говорят с исключительной любовью. Их время — весна, когда сохраняется идеальная для этих насекомых температура воздуха примерно в 25 градусов.'))
