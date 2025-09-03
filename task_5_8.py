class Item:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, name):
        if name == 'total':
            return self.price * self.quantity
        elif name == 'name':
            return object.__getattribute__(self, name).title()
        return object.__getattribute__(self, name)


class Logger:
    def __setattr__(self, name, value):
        print(f'Изменение значения атрибута {name} на {value}')
        self.__dict__[name] = value

    def __delattr__(self, name):
        print(f'Удаление атрибута {name}')
        del self.__dict__[name]


class Ord:
    def __getattr__(self, item):
        if len(item) == 1:
            return ord(item)


class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.__dict__.update(kwargs)
        self.default = default

    def __getattr__(self, item):
        return object.__getattribute__(self, 'default')


class NonNegativeObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def __setattr__(self, key, value):
        self.__dict__[key] = abs(value) if isinstance(value, int | float) else value


class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.attrs_num = 1
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            self.__dict__['attrs_num'] = self.__dict__.get('attrs_num', 0) + 1
        self.__dict__[key] = value

    def __delattr__(self, item):
        self.__dict__['attrs_num'] = self.__dict__.get('attrs_num', 0) - 1
        del self.__dict__[item]


class Const:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise AttributeError("Изменение значения атрибута невозможно")
        else:
            self.__dict__[key] = value

    def __delattr__(self, item):
        raise AttributeError("Удаление атрибута невозможно")


class ProtectedObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)

    def __getattribute__(self, item):
        if item.startswith('_'):
            raise AttributeError("Доступ к защищенному атрибуту невозможен")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key.startswith('_'):
            raise AttributeError("Доступ к защищенному атрибуту невозможен")
        else:
            object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item.startswith('_'):
            raise AttributeError("Доступ к защищенному атрибуту невозможен")
        else:
            object.__delattr__(self, item)
