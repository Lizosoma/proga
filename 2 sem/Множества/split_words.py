import string

def split_words(text):

    const = string.punctuation
    text = text.split()
    for i in range(len(text)):
        text[i] = text[i].strip(const)

    return text

if __name__ == '__main__':
    print(split_words('Вживую шелкопряды вряд ли покажутся столь милыми широкой публике, но тут о них говорят с исключительной любовью. Их время — весна, когда сохраняется идеальная для этих насекомых температура воздуха примерно в 25 градусов.'))
