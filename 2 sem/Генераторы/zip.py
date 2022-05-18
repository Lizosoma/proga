def zip(enum_1, enum_2):
    for i in range(len(enum_1)):
        yield (enum_1[i], enum_2[i])


print(list(zip([10, 20, 30], "abc")))
