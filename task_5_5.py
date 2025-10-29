class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f"FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})"

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return FoodInfo(
                self.proteins + other.proteins,
                self.fats + other.fats,
                self.carbohydrates + other.carbohydrates
            )
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return FoodInfo(
                self.proteins * other,
                self.fats * other,
                self.carbohydrates * other
            )
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return FoodInfo(
                self.proteins / other,
                self.fats / other,
                self.carbohydrates / other
            )
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return FoodInfo(
                self.proteins // other,
                self.fats // other,
                self.carbohydrates // other
            )
        return NotImplemented


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int | float):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int | float):
            return Vector(self.x / other, self.y / other)
        return NotImplemented


class SuperString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return SuperString(self.string + other.string)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return SuperString(self.string * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int):
            return SuperString(self.string[:len(self.string) // other])
        return NotImplemented

    def __lshift__(self, other):
        if isinstance(other, int):
            if other:
                return SuperString(self.string[:-other])
            else:
                return SuperString(self.string)
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):
            if other:
                return SuperString(self.string[other:])
            else:
                return SuperString(self.string)
        return NotImplemented


class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        self._normalize()

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Time(self.hours + other.hours, self.minutes + other.minutes)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.hours += other.hours
            self.minutes += other.minutes
            self._normalize()
            return self
        return NotImplemented

    def _normalize(self):
        self.hours = (self.hours + self.minutes // 60) % 24
        self.minutes = self.minutes % 60

class Path:
    def __init__(self, *args):
        self.path = list(args)

    def __repr__(self):
        return f"Path('{str(self)}')"

    def __str__(self):
        return '/'.join(map(str, self.path))

    def __truediv__(self, other):
        if isinstance(other, (str, self.__class__)):
            return Path(*self.path, other)
        else:
            return NotImplemented

    def __itruediv__(self, other):
        if isinstance(other, (str, self.__class__)):
            self.path.append(other)
            return self
        else:
            return NotImplemented



class QNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, *args):
        self.head: QNode | None = None
        self.tail: QNode | None = None
        self.add(*args)

    def add(self, *args):
        if args:
            for arg in args:
                node = QNode(arg)
                if self.head is None:
                    self.head = node
                    self.tail = node
                else:
                    self.tail.next = node
                    self.tail = node

    def pop(self):
        if self.head:
            node = self.head
            self.head = node.next
            return node.value
        return None

    def _tolist(self):
        q_list = []
        start = self.head
        while start:
            q_list.append(start.value)
            start = start.next
        return q_list

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Queue(*self._tolist(), *other._tolist())
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.add(*other._tolist())
            return self
        return NotImplemented

    def __rshift__(self, n):
        if isinstance(n, int):
            q_list = self._tolist()[n:]
            return Queue(*q_list)
        return NotImplemented

    def __str__(self):
        q_list = self._tolist()
        return ' -> '.join(map(str, q_list))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._tolist() == other._tolist()
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)
