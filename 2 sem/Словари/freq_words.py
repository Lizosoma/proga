from split_words_voc import split_words_voc
from freq_symb import freq_symb

def freq_words(text):

    vocabulary = {}
    text = split_words_voc(text)
    vocabulary = freq_symb(text)

    return vocabulary

if __name__ == '__main__':
    print(freq_words('Вживую шелкопряды вряд ли покажутся столь милыми широкой публике, но тут о них говорят с исключительной любовью. Их время — весна, когда сохраняется идеальная для этих насекомых температура воздуха примерно в 25 градусов.'))
