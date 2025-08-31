class Calculator:
    def __call__(self, a: int | float, b: int | float, operation: str):
        try:
            return eval(str(a) + operation + str(b))
        except ZeroDivisionError:
            raise ValueError('Деление на ноль невозможно')


class RaiseTo:
    def __init__(self, degree):
        self.degree = degree

    def __call__(self, x):
        return x ** self.degree


class Dice:
    def __init__(self, sides):
        self.sides = sides

    def __call__(self):
        from random import randint
        return randint(1, self.sides)


class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return self.a * x ** 2 + self.b * x + self.c


class Strip:
    def __init__(self, chars: str):
        self.chars = chars

    def __call__(self, string: str):
        return string.strip(self.chars)


class Filter:
    def __init__(self, predicate):
        self.predicate = predicate

    def __call__(self, iterable):
        return list(filter(self.predicate, iterable))


from datetime import date


class DateFormatter:
    formates = {
        "ru": "%d.%m.%Y",
        "us": "%m-%d-%Y",
        "ca": "%Y-%m-%d",
        "br": "%d/%m/%Y",
        "fr": "%d.%m.%Y",
        "pt": "%d-%m-%Y"}

    def __init__(self, country_code):
        self.country_code = country_code

    def __call__(self, d: date):
        return d.strftime(self.__class__.formates[self.country_code])


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)

class CachedFunction:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            return self.cache.get(args)
        else:
            result = self.func(*args)
            self.cache[args] = result
            return result

class SortKey:
    def __init__(self, *args):
        self.args = args

    def __call__(self, obj):
        return [getattr(obj, arg) for arg in self.args]

