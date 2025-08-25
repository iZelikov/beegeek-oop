import re

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @classmethod
    def square(cls, side):
        return cls(side, side)


class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, iterable):
        return cls(*iterable)

    @classmethod
    def from_str(cls, string: str):
        return cls.from_iterable(map(float, string.split()))


class Pet:
    _first_pet = None
    _last_pet = None
    _num_of_pets = 0

    def __init__(self, name: str):
        self.name = name
        if Pet._first_pet is None:
            Pet._first_pet = self
        Pet._last_pet = self
        Pet._num_of_pets += 1

    @classmethod
    def first_pet(cls):
        return cls._first_pet

    @classmethod
    def last_pet(cls):
        return cls._last_pet

    @classmethod
    def num_of_pets(cls):
        return cls._num_of_pets


class StrExtension:
    @staticmethod
    def remove_vowels(string: str) -> str:
        return re.sub(r'[aeiouy]', '', string, flags=re.I)

    @staticmethod
    def leave_alpha(string: str) -> str:
        return re.sub(r'[^a-zA-Z]', '', string)

    @staticmethod
    def replace_all(string: str, chars: str, char: str):
        return re.sub(rf'[{chars}]', char, string)

class CaseHelper:
    @staticmethod
    def is_snake(string: str) -> bool:
        return bool(re.search(r'^[_a-z][_a-z0-9]*$', string))

    @staticmethod
    def is_upper_camel(string: str) -> bool:
        return bool(re.search(r'^[A-Z][a-zA-z0-9]*$', string))

    @staticmethod
    def to_snake(string: str):
        snake = re.sub(r'([A-Z])', r'_\1', string)
        return snake.strip('_').lower()

    @staticmethod
    def to_upper_camel(string: str):
        return "".join(map(str.title, string.split('_')))