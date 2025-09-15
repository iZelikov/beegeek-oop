from functools import total_ordering


class UpperPrintString(str):
    def __str__(self):
        return super().__str__().upper()


class LowerString(str):
    def __new__(cls, obj: str = ''):
        return super().__new__(cls, str(obj).lower())


class FuzzyString(str):
    def __lt__(self, other):
        if isinstance(other, str):
            return self.lower() < other.lower()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, str):
            return self.lower() > other.lower()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, str):
            return self.lower() <= other.lower()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, str):
            return self.lower() >= other.lower()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, str):
            return self.lower() == other.lower()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, str):
            return self.lower() != other.lower()
        return NotImplemented

    def __contains__(self, item):
        if isinstance(item, str):
            return item.lower() in self.lower()
        return NotImplemented


class TitledText(str):
    def __new__(cls, content: str, text_title: str):
        instance = super().__new__(cls, content)
        instance._title = text_title
        return instance

    def title(self):
        return self._title


class SuperInt(int):
    def repeat(self, n=2):
        return SuperInt(("", "-")[self < 0] + str(abs(self)) * n)

    def to_bin(self):
        return f"{self:b}"

    def next(self):
        return SuperInt(self + 1)

    def prev(self):
        return SuperInt(self - 1)

    def __iter__(self):
        return map(SuperInt, str(abs(self)))


class RoundedInt(int):
    def __new__(cls, num, even=True):
        return super().__new__(cls, num + (num % 2 == even))


from itertools import chain


class AdvancedTuple(tuple):
    def __add__(self, other):
        if hasattr(other, '__iter__'):
            return AdvancedTuple(chain(self, other))
        return NotImplemented

    def __radd__(self, other):
        if hasattr(other, '__iter__'):
            return AdvancedTuple(chain(other, self))
        return NotImplemented


class  ModularTuple(tuple):
    def __new__(cls, iterable = None, size = 100):
        return super().__new__(cls, [item % size for item in iterable or []])
