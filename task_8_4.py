import functools
import random


class reverse_args:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        value = self.func(*reversed(args), **kwargs)
        return value


class MaxCallsException(Exception):
    pass


class limited_calls:
    def __init__(self, n):
        self.n = n

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if self.n > 0:
                self.n -= 1
                value = func(*args, **kwargs)
                return value
            else:
                raise MaxCallsException("Превышено допустимое количество вызовов")

        return wrapper


class takes_numbers:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        if all(isinstance(arg, int | float) for arg in (args + tuple(kwargs.values()))):
            value = self.func(*args, **kwargs)
            return value
        else:
            raise TypeError('Аргументы должны принадлежать типам int или float')


class returns:
    def __init__(self, datatype):
        self.datatype = datatype

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            if isinstance(value, self.datatype):
                return value
            else:
                raise TypeError

        return wrapper


class exception_decorator:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            value = self.func(*args, **kwargs)
            return value, None
        except Exception as e:
            return None, type(e)


class ignore_exception:
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                value = func(*args, **kwargs)
                return value
            except Exception as e:
                if type(e) in self.exceptions:
                    print(f"Исключение {type(e).__name__} обработано")
                else:
                    raise e

        return wrapper


class type_check:
    def __init__(self, types):
        self.types = types

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if all(map(lambda x: type(x[0]) is x[1], zip(args, self.types))):
                value = func(*args, **kwargs)
                return value
            else:
                raise TypeError
        return wrapper
