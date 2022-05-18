import math

class Rational:

    def __init__(self, numerator, denominator=1):
        self._n = round(numerator / math.gcd(numerator, denominator))
        self._d = round(denominator / math.gcd(numerator, denominator))

    def __str__(self):
        if self._n == 0:
            return '0'
        if self._d == 1:
            return f'{self._n}'
        if self._d == 0:
            return 'inf'
        else:
            return f'{self._n}/{self._d}'

    def as_number(self):
        if self._d != 0:
            return self._n / self._d
        else:
            return 'Ошибка'

    def __add__(self, number):
        new_n = self._n * number._d + self._d * number._n
        new_d = self._d * number._d
        return Rational(new_n, new_d)

    def __iadd__(self,number):
        new_n = self._n * number._d + self._d * number._n
        new_d = self._d * number._d
        nod = math.gcd(new_n, new_d)
        new_n = round(new_n / nod)
        new_d = round(new_d / nod)
        self._n = new_n
        self._d = new_d
        return self

    def __sub__(self, number):
        new_n = self._n * number._d - self._d * number._n
        new_d = self._d * number._d
        return Rational(new_n, new_d)

    def __isub__(self, number):
        new_n = self._n * number._d - self._d * number._n
        new_d = self._d * number._d
        nod = math.gcd(new_n, new_d)
        new_n = round(new_n / nod)
        new_d = round(new_d / nod)
        self._n = new_n
        self._d = new_d
        return self

    def __mul__(self, number):
        new_n = self._n * number._n
        new_d = self._d * number._d
        return Rational(new_n, new_d)

    def __imul__(self, number):
        new_n = self._n * number._n
        new_d = self._d * number._d
        nod = math.gcd(new_n, new_d)
        new_n = round(new_n / nod)
        new_d = round(new_d / nod)
        self._n = new_n
        self._d = new_d
        return self

    def __truediv__(self, number):
        new_n = self._n * number._d
        new_d = self._d * number._n
        return Rational(new_n, new_d)

    def __itruediv__(self, number):
        new_n = self._n * number._d
        new_d = self._d * number._n
        nod = math.gcd(new_n, new_d)
        new_n = round(new_n / nod)
        new_d = round(new_d / nod)
        self._n = new_n
        self._d = new_d
        return self

    def __pow__(self, pow):
        new_n = self._n ** pow
        new_d = self._d ** pow
        return Rational(new_n, new_d)

    def __ipow__(self, pow):
        new_n = self._n ** pow
        new_d = self._d ** pow
        nod = math.gcd(new_n, new_d)
        new_n = round(new_n / nod)
        new_d = round(new_d / nod)
        self._n = new_n
        self._d = new_d
        return self

    def __radd__(self, number):
        number = Rational(number, 1)
        return number + self

    def __rsub__(self, number):
        number = Rational(number, 1)
        return number - self

    def __rmul__(self, number):
        number = Rational(number, 1)
        return number * self

    def __rtruediv__(self, number):
        number = Rational(number, 1)
        return number / self

    def __eq__(self, number):
        x = self._n / self._d
        y = number._n / number._d
        return x == y

    def __ne__(self, number):
        return not self.__eq__(number)

    def __lt__(self, number):
        x = self._n / self._d
        y = number._n / number._d
        return x < y

    def __le__(self, number):
        return self.__lt__(number) or self.__eq__(number)

    def __gt__(self, number):
        return not self.__lt__(number)

    def __ge__(self, number):
        return not self.__lt__(number) or self.__eq__(number)

    def _get_n(self):
        return self._n

    def _get_d(self):
        return self._d

    ONE = 1
    ZERO = 0

    def irreducible(n):
        for m in range(n + 1):
            if math.gcd(m, n) == 1:
                if n == 1 and m == 1:
                    continue
                yield f'{m}/{n}'

def f(n):
    a = 0
    for i in range(1, n + 1):
        a += 1 / i
    return a


a = Rational(18, 21)

print(a)

print(f'As number: {a.as_number()}')

n_1 = Rational(1, 6)
n_2 = Rational(1, 3)
n_3 = n_2 + n_1
print(f'__add__: {n_3}')
n_3 = n_1 - n_2
print(f'__sub__: {n_3}')
n_3 = n_1 * n_2
print(f'__mul__: {n_3}')
n_3 = n_1 / n_2
print(f'__truediv__: {n_3}')
pow = 2
n_2 = n_1 ** pow
print(f'__pow__: {n_2}')

n_1 = Rational(1, 6)
n_2 = Rational(1, 3)
n_1 += n_2
print(f'__iadd__: {n_1}')
n_1 -= n_2
print(f'__isub__: {n_1}')
n_1 *= n_2
print(f'__imul__: {n_1}')
n_1 /= n_2
print(f'__itruediv__: {n_1}')
pow = 2
n_1 **= pow
print(f'__ipow__: {n_1}')

n_1 = Rational(1, 6)
n_2 = Rational(2)
n_3 = n_1 + n_2
print(f'__radd__: {n_3}')
n_3 = n_1 - n_2
print(f'__rsub__: {n_3}')
n_3 = n_1 * n_2
print(f'__rmul__: {n_3}')
n_3 = n_1 / n_2
print(f'__rtruediv__: {n_3}')

n_1 = Rational(1, 6)
n_2 = Rational(1, 3)
print(f'__eq__: {n_1 == n_2}')
print(f'__ne__: {n_1 != n_2}')
print(f'__lt__: {n_1 < n_2}')
print(f'__le__: {n_1 <= n_2}')
print(f'__gt__: {n_1 > n_2}')
print(f'__ge__: {n_1 >= n_2}')

print(f'f: {f(3)}')

print(f'_get_n: {a._get_n()}')
print(f'_gen_d: {a._get_d()}')

print(f'ONE: {Rational.ONE}')
print(f'ZERO: {Rational.ZERO}')

print(f'irreducible: {list(sorted(Rational.irreducible(10)))}')
