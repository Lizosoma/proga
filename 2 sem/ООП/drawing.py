class Drawing:

    def __init__(self, string, column, symbol):
        self.string = string
        self.column = column
        self.symbol = symbol
        self.picture = [[symbol] * string for i in range(column)]

    def Print(self):
        for i in range(self.column):
            print(''.join(map(str, self.picture[i])))

    def setPoint(self, x, y, char):
        self.picture[x - 1][y - 1] = char

    def drawHorizontalLine(self, y_1, y_2, x, char):
        for v in range(y_1, y_2 + 1):
            self.setPoint(x, v, char)

    def drawVerticalLine(self, x_1, x_2, y, char):
        for h in range(x_1, x_2 + 1):
            self.setPoint(h, y, char)

    def drawRectangle(self, x_1, y_1, x_2, y_2, char):
        self.drawVerticalLine(y_1, y_2, x_1, char)
        self.drawVerticalLine(y_1, y_2, x_2, char)
        self.drawHorizontalLine(x_1, x_2, y_1, char)
        self.drawHorizontalLine(x_1, x_2, y_2, char)

    def someLine(self, x_1, y_1, x_2, y_2, char):
        dis_x = abs(x_2 - x_1)
        dis_y = abs(y_2 - y_1)
        if x_1 < x_2:
            dir_x = 1
        else:
            dir_x = -1
        if y_1 < y_2:
            dir_y = 1
        else:
            dir_y = -1

        error = dis_x - dis_y

        self.setPoint(y_2, x_2, char)
        while x_1 != x_2 or y_1 != y_2:
            self.setPoint(y_1, x_1, char)
            error_2 = error * 2

            if error_2 > -dis_y:
                error -= dis_y
                x_1 += dir_x

            if error_2 < dis_x:
                error += dis_x
                y_1 += dir_y

    def Circle(self, x_0, y_0, r, char):
        x = 0
        y = r
        delta = 1 - 2 * r
        error = 0
        while (y >= x):
            self.setPoint(x_0 + x, y_0 + y, char)
            self.setPoint(x_0 + x, y_0 - y, char)
            self.setPoint(x_0 - x, y_0 + y, char)
            self.setPoint(x_0 - x, y_0 - y, char)
            self.setPoint(x_0 + y, y_0 + x, char)
            self.setPoint(x_0 + y, y_0 - x, char)
            self.setPoint(x_0 - y, y_0 + x, char)
            self.setPoint(x_0 - y, y_0 - x, char)
            error = 2 * (delta + y) - 1
            if delta < 0 and error <= 0:
                x += 1
                delta += 2 * x + 1
                continue
            if delta > 0 and error > 0:
                y -= 1
                delta -= 2 * y + 1
                continue
            x += 1
            y -= 1
            delta += 2 * (x - y)

    def draw(self, x, y, drawing):
        strings = drawing.picture
        columns = drawing.picture[0]
        for i in range(len(strings)):
            for j in range(len(columns)):
                point = self.picture[y - 1 + i][x - 1 + j]
                if point == self.symbol:
                    self.picture[y - 1 + i][x - 1 + j] = drawing.picture[i][j]


# a = Drawing(20, 11, '🌚')
# a.Print()
# a.setPoint(3, 2, '🌝')
# a.Print()
# a.drawVerticalLine(4, 10, 5, '🌞')
# a.Print()
# a.drawHorizontalLine(4, 10, 6, '🌞')
# a.Print()
# a.drawRectangle(1, 1, 6, 10, '🌞')
# a.Print()
# a.someLine(2, 2, 11, 9, '🌝')
# a.Print()
# a.Circle(6, 10, 4, '🌝')
# a.Print()
# a_1 = Drawing(9, 9, '🌚')
# a_1.drawRectangle(3, 3, 5, 5)
# a.draw(7, 3, a_1)
# a.Print()
house = Drawing(30, 23, '. ')
house.drawRectangle(1, 1, 30, 23, '░ ')
house.drawVerticalLine(2, 22, 2, '░ ')
house.drawVerticalLine(2, 22, 29, '░ ')
house.drawVerticalLine(4, 20, 25, '░ ')
house.drawRectangle(5, 3, 26, 21, '░ ')
house.Circle(7, 15, 3, '░ ')
house.drawHorizontalLine(13, 17, 4, '░ ')
house.drawHorizontalLine(5, 11, 8, '░ ')
house.drawHorizontalLine(19, 25, 8, '░ ')
house.drawVerticalLine(15, 20, 6, '░ ')
house.drawVerticalLine(14, 20, 7, '░ ')
house.drawVerticalLine(14, 20, 8, '░ ')
house.drawVerticalLine(12, 20, 9, '░ ')
house.drawVerticalLine(7, 13, 10, '░ ')
house.drawVerticalLine(5, 13, 11, '░ ')
house.drawVerticalLine(13, 20, 24, '░ ')
house.drawVerticalLine(13, 20, 23, '░ ')
house.drawVerticalLine(12, 20, 22, '░ ')
house.drawVerticalLine(9, 20, 21, '░ ')
house.drawVerticalLine(6, 20, 20, '░ ')
house.drawVerticalLine(5, 20, 19, '░ ')
house.drawVerticalLine(5, 20, 18, '░ ')
house.drawVerticalLine(9, 13, 12, '░ ')
house.drawHorizontalLine(6, 24, 16, '░ ')
house.drawHorizontalLine(6, 11, 17, '░ ')
house.drawHorizontalLine(15, 17, 17, '░ ')
house.drawHorizontalLine(10, 13, 18, '░ ')
house.drawHorizontalLine(13, 17, 19, '░ ')
house.drawHorizontalLine(13, 17, 20, '░ ')
house.setPoint(12, 13, '░ ')
house.drawHorizontalLine(12, 18, 11, '░ ')
house.drawHorizontalLine(12, 18, 10, '░ ')
house.setPoint(5, 12, '░ ')
house.draw(1, 1, house)
house.Print()
