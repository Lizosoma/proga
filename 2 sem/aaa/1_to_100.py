def g(file):
    
    with open(file, mode="w", encoding="utf8") as f:
        for x in range(1, 101):
            f.write(f'{x}\n')

g(file = '1_to_100.txt')
