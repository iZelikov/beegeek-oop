from datetime import date
from functools import singledispatchmethod


class Processor:
    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @process.register(int)
    @process.register(float)
    @staticmethod
    def process_number(data: int | float) -> int | float:
        return data * 2

    @process.register(str)
    @staticmethod
    def process_str(data: str) -> str:
        return data.upper()

    @process.register(list)
    @staticmethod
    def process_list(data: list) -> list:
        return sorted(data)

    @process.register(tuple)
    @staticmethod
    def process_tuple(data: tuple) -> tuple:
        return tuple(sorted(data))


class Negator:

    @singledispatchmethod
    @staticmethod
    def neg(arg):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def neg_number(arg):
        return -arg

    @neg.register(bool)
    @staticmethod
    def neg_bool(arg):
        return not arg


class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(arg):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register(int)
    @staticmethod
    def format_int(arg: int):
        print(f'Целое число: {arg}')

    @format.register(float)
    @staticmethod
    def format_float(arg: float):
        print(f'Вещественное число: {arg}')

    @format.register(list)
    @staticmethod
    def format_list(arg: list):
        print(f'Элементы списка: {", ".join(map(str, arg))}')

    @format.register(tuple)
    @staticmethod
    def format_tuple(arg: tuple):
        print(f'Элементы кортежа: {", ".join(map(str, arg))}')

    @format.register(dict)
    @staticmethod
    def format_dict(arg: dict):
        print(f'Пары словаря: {", ".join(map(str, arg.items()))}')


class BirthInfo:
    @singledispatchmethod
    def __init__(self, d):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(date)
    def __init__date(self, date_obj):
        self.birth_date: date = date_obj

    @__init__.register(str)
    def __init__iso_str(self, date_string):
        try:
            self.birth_date: date = date.fromisoformat(date_string)
        except:
            raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(list)
    @__init__.register(tuple)
    def __init__array(self, date_array):
        try:
            self.birth_date = date(*date_array)
        except:
            raise TypeError('Аргумент переданного типа не поддерживается')

    @property
    def age(self):
        today = date.today()
        current_age = today.year - self.birth_date.year - 1
        current_age += (today.month, today.day) >= (self.birth_date.month, self.birth_date.day)
        return current_age

