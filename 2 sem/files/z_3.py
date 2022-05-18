def z_3():

    with open('text.txt', mode='rb') as f:

        bities = {}
        bities_sorted = []

        text = f.read().split()
        for word in text:
            array = bytearray(word)
            for byte in array:
                if byte in bities:
                    bities[byte] += 1
                else:
                    bities[byte] = 1

        for pair in bities.items():
            a, b = pair
            bities_sorted.append([b, a])
            bities_sorted.sort()
        return max(bities_sorted)[1]

print(z_3())
