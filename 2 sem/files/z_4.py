def z_4(read_file, write_file):

    with open(read_file, mode='r', encoding='utf8') as f:

        text = f.read()
        new_str = ''

        for symbol in text:
            new_str += symbol * 2

        with open(write_file, mode='w', encoding='utf8') as g:

            g.write(new_str)

z_4('text.txt', 'new_text.txt')