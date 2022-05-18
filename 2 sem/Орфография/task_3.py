from task_2 import task_2

def task_3(wr_text):

    with open(wr_text, mode="w", encoding="utf8") as w:

        w.write(str(task_2('words_alpha.txt', 'eng_text.txt')))


print(task_2('words_alpha.txt', 'eng_text.txt'))
task_3(wr_text='written_text')