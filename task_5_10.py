class ColoredPoint:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    def __repr__(self):
        return f"ColoredPoint({self.x}, {self.y}, '{self.color}')"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.x, self.y, self.color) == (other.x, other.y, other.color)
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash((self.x, self.y, self.color))


class Row:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        raise AttributeError('Установка нового атрибута невозможна')

    def __delattr__(self, item):
        raise AttributeError('Удаление атрибута невозможно')

    def __repr__(self):
        return f"Row({', '.join(f'{k}={repr(v)}' for k, v in self.__dict__.items())})"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return repr(self) == repr(other)
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(repr(self))
