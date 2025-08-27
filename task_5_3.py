from functools import total_ordering


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, tuple) and len(other) == 2:
            return self.x == other[0] and self.y == other[1]

        return NotImplemented

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'


@total_ordering
class Word:
    def __init__(self, word: str):
        self.word = word

    def __repr__(self):
        return f"Word('{self.word}')"

    def __str__(self):
        return f'{self.word.title()}'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return len(self.word) == len(other.word)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return len(self.word) < len(other.word)
        return NotImplemented


@total_ordering
class Month:
    def __init__(self, year: int, month: int):
        self.year = year
        self.month = month

    def __repr__(self):
        return f"Month({self.year}, {self.month})"

    def __str__(self):
        return f"{self.year}-{self.month}"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.year, self.month) == (other.year, other.month)
        elif isinstance(other, tuple):
            return (self.year, self.month) == other
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return (self.year, self.month) < (other.year, other.month)
        elif isinstance(other, tuple):
            return (self.year, self.month) < other
        return NotImplemented


@total_ordering
class Version:
    def __init__(self, version: str):
        self.version = version
        self.version = ".".join(map(str, self._to_list()))

    def __repr__(self):
        return f"Version('{self.version}')"

    def __str__(self):
        return self.version

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._to_list() == other._to_list()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self._to_list() < other._to_list()
        return NotImplemented

    def _to_list(self):
        l = list(map(int, self.version.split('.')))
        l += [0] * (3 - len(l))
        return l
