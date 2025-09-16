from collections import UserList, UserDict, UserString


class DefaultList(UserList):
    def __init__(self, iterable=None, default=None):
        super().__init__(iterable or [])
        self._default = default

    def __getitem__(self, idx):
        try:
            return self.data[idx]
        except IndexError:
            return self._default


class EasyDict(dict):
    def __getattr__(self, item):
        return self.__getitem__(item)


class TwoWayDict(UserDict):
    def __setitem__(self, key, value):
        self.data[key] = value
        self.data[value] = key


class AdvancedList(list):
    def join(self, delimiter=" "):
        return delimiter.join(map(str, self))

    def map(self, func):
        self[:] = map(func, self)

    def filter(self, func):
        self[:] = filter(func, self)


class NumberList(UserList):
    def __init__(self, iterable):
        super().__init__()
        self.extend(iterable)

    def __setitem__(self, key, item):
        super().__setitem__(key, self.validate(item))

    def append(self, item):
        super().append(self.validate(item))

    def extend(self, iterable):
        from itertools import tee
        it1, it2 = tee(iterable or [])
        if all(map(lambda x: isinstance(x, int | float), it1)):
            super().extend(it2)
        else:
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')

    def insert(self, i, item):
        super().insert(i, self.validate(item))

    def __iadd__(self, other):
        self.extend(other)
        return self

    @staticmethod
    def validate(value):
        if isinstance(value, int | float):
            return value
        else:
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')


class ValueDict(dict):

    def _map(self, value):
        return map(lambda y: y[0], (filter(lambda x: x[1] == value, self.items())))

    def key_of(self, value):
        return next(self._map(value), None)

    def keys_of(self, value):
        return list(self._map(value))

class BirthdayDict(UserDict):
    def __setitem__(self, key, value):
        if value in self.values():
            print(f"Хей, {key}, не только ты празднуешь день рождения в этот день!")
        super().__setitem__(key,value)

class MutableString(UserString):
    def lower(self):
        self.data = self.data.lower()

    def upper(self):
        self.data = self.data.upper()

    def sort(self, *args, **kwargs):
        self.data = "".join(sorted(self.data, *args, **kwargs))

    def __setitem__(self, key, value):
        temp_list = list(self.data)
        temp_list[key] = value
        self.data = "".join(temp_list)

    def __delitem__(self, key):
        temp_list = list(self.data)
        del temp_list[key]
        self.data = "".join(temp_list)