class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __int__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

    def __float__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __complex__(self):
        return complex(self.x, self.y)


class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return self.temperature * 9 / 5 + 32

    @classmethod
    def from_fahrenheit(cls, tf):
        return Temperature(5 / 9 * (tf - 32))

    def __str__(self):
        return f"{round(self.temperature, 2)}°C"

    def __bool__(self):
        return self.temperature > 0

    def __int__(self):
        return int(self.temperature)

    def __float__(self):
        return float(self.temperature)


from functools import total_ordering
from copy import copy


@total_ordering
class RomanNumeral:
    romans = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D',
              900: 'CM', 1000: 'M'}

    def __init__(self, number: str):
        self.decimal = self.roman_to_decimal(number)

    @staticmethod
    def _from_decimal(number: int):
        new_obj = RomanNumeral('I')
        new_obj.decimal = number
        return new_obj

    @staticmethod
    def roman_to_decimal(roman_str: str):
        total = 0
        romans = copy(RomanNumeral.romans)
        while romans:
            current = romans.popitem()
            while roman_str.startswith(current[1]):
                total += current[0]
                roman_str = roman_str.replace(current[1], "", 1)
        if roman_str:
            raise ValueError("Некорректное римское число")
        else:
            return total

    @staticmethod
    def decimal_to_roman(decimal: int):
        roman_list = []
        romans = copy(RomanNumeral.romans)
        while romans:
            current = romans.popitem()
            while decimal >= current[0]:
                decimal -= current[0]
                roman_list.append(current[1])
        return "".join(roman_list)

    def __str__(self):
        return self.decimal_to_roman(self.decimal)

    def __int__(self):
        return self.decimal

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.decimal == other.decimal
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.decimal < other.decimal
        else:
            return NotImplemented

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self._from_decimal(self.decimal + other.decimal)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return self._from_decimal(self.decimal - other.decimal)
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.decimal += other.decimal
            return self
        else:
            return NotImplemented

    def __isub__(self, other):
        if isinstance(other, self.__class__):
            self.decimal -= other.decimal
            return self
        else:
            return NotImplemented
