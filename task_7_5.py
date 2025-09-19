from abc import abstractmethod, ABC
from collections import UserString, UserList
from collections.abc import Iterable, Iterator, Sequence, MutableSequence


class Middle(ABC):
    @abstractmethod
    def get_average(self, users=True):
        pass

    def __init__(self, user_votes, expert_votes):
        self.user_votes = user_votes  # пользовательские оценки
        self.expert_votes = expert_votes  # оценки критиков

    def get_correct_user_votes(self):
        """Возвращает нормализованный список пользовательских оценок
        без слишком низких и слишком высоких значений"""
        return [vote for vote in self.user_votes if 10 < vote < 90]

    def get_correct_expert_votes(self):
        """Возвращает нормализованный список оценок критиков
        без слишком низких и слишком высоких значений"""
        return [vote for vote in self.expert_votes if 5 < vote < 95]


class Average(Middle):

    def get_average(self, users=True):
        """Возвращает среднее арифметическое пользовательских оценок или
        оценок критиков в зависимости от значения параметра users"""
        if users:
            votes = self.get_correct_user_votes()
        else:
            votes = self.get_correct_expert_votes()

        return sum(votes) / len(votes)


class Median(Middle):

    def get_average(self, users=True):
        """Возвращает медиану пользовательских оценок или
        оценок критиков в зависимости от значения параметра users"""
        if users:
            votes = sorted(self.get_correct_user_votes())
        else:
            votes = sorted(self.get_correct_expert_votes())

        return votes[len(votes) // 2]


class Harmonic(Middle):

    def get_average(self, users=True):
        """Возвращает среднее гармоническое пользовательских оценок или
        оценок критиков в зависимости от значения параметра users"""
        if users:
            votes = self.get_correct_user_votes()
        else:
            votes = self.get_correct_expert_votes()

        return len(votes) / sum(map(lambda vote: 1 / vote, votes))


class ChessPiece(ABC):

    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    @abstractmethod
    def can_move(self, horizontal, vertical):
        pass

    def _delta(self, horizontal, vertical):
        dx = abs(ord(self.horizontal) - ord(horizontal))
        dy = abs(self.vertical - vertical)
        return dx, dy


class King(ChessPiece):
    def can_move(self, horizontal, vertical):
        dx, dy = self._delta(horizontal, vertical)
        return bool((dx or dy) and (dx <= 1 and dy <= 1))


class Knight(ChessPiece):
    def can_move(self, horizontal, vertical):
        dx, dy = self._delta(horizontal, vertical)
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)


class Validator(ABC):
    def __set_name__(self, owner, name):
        self._attr = name

    def __set__(self, instance, value):
        instance.__dict__[self._attr] = self.validate(value)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        try:
            return instance.__dict__[self._attr]
        except:
            raise AttributeError('Атрибут не найден')

    @abstractmethod
    def validate(self, value):
        return value


class Number(Validator):
    def __init__(self, minvalue=float('-inf'), maxvalue=float('inf')):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, int | float):
            raise TypeError('Устанавливаемое значение должно быть числом')
        elif value < self.minvalue:
            raise ValueError(f'Устанавливаемое число должно быть больше или равно {self.minvalue}')
        elif value > self.maxvalue:
            raise ValueError(f'Устанавливаемое число должно быть меньше или равно {self.maxvalue}')
        return value


class String(Validator):
    def __init__(self, minsize=float('-inf'), maxsize=float('inf'), predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError('Устанавливаемое значение должно быть строкой')
        elif len(value) < self.minsize:
            raise ValueError(f'Длина устанавливаемой строки должна быть больше или равна {self.minsize}')
        elif len(value) > self.maxsize:
            raise ValueError(f'Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}')
        elif self.predicate:
            if not self.predicate(value):
                raise ValueError('Устанавливаемая строка не удовлетворяет дополнительным условиям')
        return value


def is_iterable(obj):
    return isinstance(obj, Iterable)


def is_iterator(obj):
    return isinstance(obj, Iterator)


class CustomRange(Sequence):
    def __init__(self, *items):
        self.data = []
        for item in items:
            if isinstance(item, int):
                self.data.append(item)
            elif isinstance(item, str):
                start, end = tuple(map(int, item.split('-')))
                self.data.extend(range(start, end + 1))

    def __getitem__(self, key):
        return self.data[key]

    def __len__(self):
        return len(self.data)


class BitArray(Sequence):
    def __init__(self, data=None):
        self._data = list(data or [])

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __invert__(self):
        return self.__class__(int(not x) for x in self._data)

    def __or__(self, other):
        if isinstance(other, BitArray) and len(self) == len(other):
            return self.__class__(a | b for a, b in zip(self._data, other))
        else:
            return NotImplemented

    def __and__(self, other):
        if isinstance(other, BitArray) and len(self) == len(other):
            return self.__class__(a & b for a, b in zip(self._data, other))
        else:
            return NotImplemented

    def __str__(self):
        return str(self._data)


class DNA(UserString):
    compliments = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

    def __getitem__(self, idx):
        return self.data[idx], self.compliments[self.data[idx]]

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.data + other.data)
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.data == other.data
        else:
            return NotImplemented


class SortedList(UserList):
    def __init__(self, iterable=()):
        super().__init__(sorted(iterable))

    def add(self, obj):
        for i, v in enumerate(self.data):
            if obj < v:
                self.data.insert(i, obj)
                break
        else:
            self.data.append(obj)

    def discard(self, obj):
        self.data = [i for i in self.data if i != obj]

    def update(self, iterable):
        import math
        if len(iterable) < math.log2(len(self.data)):
            for i in iterable:
                self.add(i)
        else:
            self.data.extend(iterable)
            self.data.sort()

    def append(self, item):
        raise NotImplementedError

    def insert(self, i, item):
        raise NotImplementedError

    def extend(self, other):
        raise NotImplementedError

    def reverse(self):
        raise NotImplementedError

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __reversed__(self):
        raise NotImplementedError

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.data)})"

    def __mul__(self, n):
        if isinstance(n, int):
            return self.__class__(super().__mul__(n))
        else:
            return NotImplemented

    def __imul__(self, n):
        if isinstance(n, int):
            self.data *= n
            self.data.sort()
            return self
        else:
            return NotImplemented

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.data + other.data)
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.update(other.data)
            return self
        else:
            return NotImplemented
