def line(x):

    prev_symb = ''
    k = 0
    for i in x:
        if i == 'A' and prev_symb == 'B' or i == 'B' and prev_symb == 'A':
            k += 1
        prev_symb = i

    return k

print(line('xxxAyyyBxxxAByyyBAxxxABA'))

