class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return (f'{self.name} {self.surname}')

    @fullname.setter
    def fullname(self, value: str):
        self.name, self.surname = value.split()


def hash_function(password):
    hash_value = 0
    for char, index in zip(password, range(len(password))):
        hash_value += ord(char) * index
    return hash_value % 10 ** 9


class Account:
    def __init__(self, login, password):
        self._login = login
        self._hash = hash_function(password)

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        raise AttributeError('Изменение логина невозможно')

    @property
    def password(self):
        return self._hash

    @password.setter
    def password(self, value):
        self._hash = hash_function(value)


class QuadraticPolynomial:
    def __init__(self, a: float, b: float, c: float):
        self.coefficients = (a, b, c)

    @property
    def x1(self):
        d = self.b ** 2 - 4 * self.a * self.c
        return (-self.b - d ** 0.5) / (2 * self.a) if d >= 0 else None

    @property
    def x2(self):
        d = self.b ** 2 - 4 * self.a * self.c
        return (-self.b + d ** 0.5) / (2 * self.a) if d >= 0 else None

    @property
    def view(self):
        return f'{self.a}x^2 {'+-'[self.b < 0]} {abs(self.b)}x {'+-'[self.c < 0]} {abs(self.c)}'

    @property
    def coefficients(self):
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, value):
        self.a, self.b, self.c = value


class Color:
    def __init__(self, hexcode):
        self.hexcode = hexcode

    @property
    def hexcode(self):
        return f'{self.r * 2 ** 16 + self.g * 2 ** 8 + self.b:06X}'

    @hexcode.setter
    def hexcode(self, hexcode):
        self.r = int(hexcode[:2], 16)
        self.g = int(hexcode[2:4], 16)
        self.b = int(hexcode[4:], 16)
