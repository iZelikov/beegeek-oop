from functools import singledispatchmethod
import re


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.author}, {self.year})"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __repr__(self):
        return f'Rectangle({self.length}, {self.width})'

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __str__(self):
        return f'Вектор на плоскости с координатами ({self.x}, {self.y})'


class IPAddress:
    @singledispatchmethod
    def __init__(self, ipaddress):
        raise TypeError('Неверный формат адреса')

    @__init__.register(str)
    def __init__str(self, ipaddress):
        self.ipaddress = ipaddress

    @__init__.register(tuple)
    @__init__.register(list)
    def __init__arr(self, ipaddress):
        self.ipaddress = '.'.join(map(str, ipaddress))

    def __str__(self):
        return self.ipaddress

    def __repr__(self):
        return f"IPAddress('{self.ipaddress}')"

class PhoneNumber:
    def __init__(self, phone_number: str):
        self.phone_number = re.sub(r'\D', '', phone_number)

    def __str__(self):
        return re.sub(r'(\d{3})(\d{3})(\d{4})', r'(\1) \2-\3', self.phone_number)

    def __repr__(self):
        return f"PhoneNumber('{self.phone_number}')"

class AnyClass:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return f'AnyClass: ' + ', '.join(f'{k}={repr(v)}' for k,v in self.__dict__.items())

    def __repr__(self):
        return f"AnyClass({', '.join(f'{k}={repr(v)}' for k,v in self.__dict__.items())})"

