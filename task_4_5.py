from tkinter.font import names


class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def get_perimeter(self) -> float:
        return 2 * (self.length + self.width)

    def get_area(self) -> float:
        return self.length * self.width

    perimeter: float = property(fget=get_perimeter)
    area: float = property(fget=get_area)


class HourClock:
    def __init__(self, hours: int):
        self.hours = hours

    def get_hour(self) -> int:
        return self._hours

    def set_hours(self, hours: int):
        if isinstance(hours, int) and 1 <= hours <= 12:
            self._hours = hours
        else:
            raise ValueError('Некорректное время')

    hours = property(get_hour, set_hours)

class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def get_fullname(self)-> str:
        return f'{self.name} {self.surname}'

    def set_fullname(self, fullname: str):
        self.name, self.surname = fullname.split()

    fullname = property(get_fullname, set_fullname)

