import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'


class Circle:
    def __init__(self, radius, center):
        self.radius = radius
        self.center = center

    def __str__(self):
        return f'{self.center}, r = {self.radius}'


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}, {self.price}$'


class ShoppingCart:
    def __init__(self, items: list[Item] = None):
        self.items = items or []

    def add(self, item: Item):
        self.items.append(item)

    def total(self):
        return sum(map(lambda x: x.price, self.items))

    def remove(self, item_name: str):
        self.items = list(filter(lambda x: x.name != item_name, self.items))

    def __str__(self):
        return "\n".join(map(str, self.items))


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.suit}{self.rank}'


class Deck:
    suits = ["♣", '♢', "♡", '♠']
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        if len(self.cards) == 52:
            random.shuffle(self.cards)
        else:
            raise ValueError("Перемешивать можно только полную колоду")

    def deal(self):
        try:
            return self.cards.pop()
        except IndexError:
            raise ValueError("Все карты разыграны")

    def __str__(self):
        return f"Карт в колоде: {len(self.cards)}"


from collections import OrderedDict


class Queue:
    def __init__(self, pairs: list[tuple] | dict = None):
        self._data = OrderedDict() if pairs is None else OrderedDict(pairs)

    def add(self, item: tuple):
        if item[0] in self._data:
            self._data.move_to_end(item[0])
        self._data[item[0]] = item[1]

    def pop(self):
        try:
            return self._data.popitem(last=False)
        except KeyError:
            raise KeyError("Очередь пуста")

    def __repr__(self):
        return self.__class__.__name__ + f"([{', '.join(map(repr, self._data.items()))}])"

    def __len__(self):
        return len(self._data)


from itertools import pairwise


class Lecture:
    def __init__(self, topic: str, start_time: str, duration: str):
        self.topic = topic
        self.start_time = start_time
        self.duration = duration

    @staticmethod
    def convert(time: str | int):
        if isinstance(time, str):
            h, m = map(int, time.split(':'))
            return h * 60 + m
        elif isinstance(time, int):
            return f"{time // 60:02}:{time % 60:02}"

    def __and__(self, other):
        if isinstance(other, Lecture):
            return self - other < 0 and other - self < 0
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Lecture):
            s1 = self.convert(self.start_time)
            s2 = self.convert(other.start_time)
            d2 = self.convert(other.duration)
            return s1 - (s2 + d2)
        else:
            return NotImplemented

    def __add__(self, other):
        if isinstance(other, Lecture):
            return self.convert(self.duration) + other.convert(other.duration)
        elif isinstance(other, int):
            return self.convert(self.duration) + other
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, int):
            return self.convert(self.duration) + other
        return NotImplemented


class Conference:
    def __init__(self):
        self.lectures: list[Lecture] = []

    def add(self, lecture: Lecture):
        if any(map(lambda another_lecture: lecture & another_lecture, self.lectures)):
            raise ValueError('Провести выступление в это время невозможно')
        else:
            self.lectures.append(lecture)

    def total(self):
        return Lecture.convert(sum(self.lectures))

    def longest_lecture(self):
        return max(self.lectures, key=lambda x: Lecture.convert(x.duration)).duration

    def longest_break(self):
        sl = sorted(self.lectures, key=lambda x: Lecture.convert(x.start_time))
        if len(sl) > 1:
            return Lecture.convert(max(map(lambda x: x[1] - x[0], pairwise(sl))))
        else:
            return '00:00'
