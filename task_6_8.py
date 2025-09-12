from keyword import kwlist

class NonKeyword:
    def __init__(self, name):
        self._attr = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        try:
            return instance.__dict__[self._attr]
        except:
            raise AttributeError("Атрибут не найден")

    def __set__(self, instance, value):
        if value in kwlist:
            raise ValueError("Некорректное значение")
        else:
            instance.__dict__[self._attr] = value


class NonNegativeInteger:
    def __init__(self, name, default = None):
        self._attr = name
        self._default = default

    def __get__(self, instance, owner):
        if instance is None:
            return self
        try:
            return instance.__dict__[self._attr]
        except Exception:
            if self._default is None:
                raise AttributeError('Атрибут не найден')
            else:
                return self._default
    def __set__(self, instance, value):
        if isinstance(value, int) and value >= 0:
            instance.__dict__[self._attr] = value
        else:
            raise ValueError('Некорректное значение')

class MaxCallsException(Exception):
    pass

class LimitedTakes:
    def __init__(self, times):
        self._times = times

    def __set_name__(self, owner, name):
        self._attr = name

    def __get__(self, instance, owner):
        if self._times <=0:
            raise MaxCallsException("Превышено количество доступных обращений")
        else:
            self._times -= 1
            if instance is None:
                return self
            try:
                return instance.__dict__[self._attr]
            except:
                raise AttributeError("Атрибут не найден")

    def __set__(self, instance, value):
        instance.__dict__[self._attr] = value

class TypeChecked:
    def __init__(self, *types):
        self._types = types

    def __set_name__(self, owner, name):
        self._attr = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        try:
            return instance.__dict__[self._attr]
        except:
            raise AttributeError("Атрибут не найден")
    def __set__(self, instance, value):
        if isinstance(value, self._types):
            instance.__dict__[self._attr] = value
        else:
            raise TypeError('Некорректное значение')

from random import randint
class RandomNumber:
    def __init__(self, start: int, end: int, cache = False):
        self._start = start
        self._end = end
        self._cache = cache
        self._value = None

    def __set_name__(self, owner, name):
        self._attr = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self._cache:
            if self._value is None:
                self._value = randint(self._start, self._end)
            return self._value
        else:
            return randint(self._start, self._end)

    def __set__(self, instance, value):
        raise  AttributeError("Изменение невозможно")

class Versioned:
    def __set_name__(self, instance, name):
        self._attr = name
        self._history = {}

    def __get__(self, instance, owner):
        if instance is None:
            return self
        try:
            return instance.__dict__[self._attr]
        except:
            raise AttributeError("Атрибут не найден")

    def __set__(self, instance, value):
        instance.__dict__[self._attr] = value
        self._history.setdefault(instance, []).append(value)

    def get_version(self, instance, n):
        return self._history[instance][n-1]

    def set_version(self, instance, n):
        instance.__dict__[self._attr] = self.get_version(instance, n)