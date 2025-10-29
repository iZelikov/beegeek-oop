from abc import ABC, abstractmethod
from collections import UserDict
from copy import deepcopy
from dataclasses import dataclass
from itertools import count as cnt
import re
from random import randrange


class anything:
    __ne__ = __lt__ = __gt__ = __le__ = __ge__ = __eq__ = lambda *args: True


class Vector:
    def __init__(self, *args):
        self.args = tuple(args)
        self.length = len(args)

    def __repr__(self):
        return f"{self.args}"

    def __add__(self, other):
        if isinstance(other, Vector):
            if self.length == other.length:
                return Vector(*(x + y for x, y in zip(self.args, other.args)))
            else:
                raise ValueError("Векторы должны иметь равную длину")
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            if self.length == other.length:
                return Vector(*(x - y for x, y in zip(self.args, other.args)))
            else:
                raise ValueError("Векторы должны иметь равную длину")
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vector):
            if self.length == other.length:
                return sum(x * y for x, y in zip(self.args, other.args))
            else:
                raise ValueError("Векторы должны иметь равную длину")
        elif isinstance(other, (int, float)):
            return Vector(*(x * other for x in self.args))
        else:
            return NotImplemented

    def norm(self):
        return sum(x ** 2 for x in self.args) ** 0.5

    def __eq__(self, other):
        if isinstance(other, Vector):
            if self.length != other.length:
                raise ValueError("Векторы должны иметь равную длину")
            return self.args == other.args
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Vector):
            if self.length != other.length:
                raise ValueError("Векторы должны иметь равную длину")
            return self.args != other.args
        else:
            return NotImplemented


class CaesarCipher:
    a = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, shift: int):
        self.shift = shift

    def _translate(self, char, direction=1):
        if char.lower() in self.a:
            new_char = self.a[(self.a.index(char.lower()) + self.shift * direction) % len(self.a)]
            return (new_char, new_char.upper())[char.isupper()]
        return char

    def encode(self, text, direction=1):
        return "".join([self._translate(c, direction) for c in text])

    def decode(self, text):
        return self.encode(text, -1)


class Progression(ABC):
    def __init__(self, start, step):
        self.start = start
        self.step = step

    @abstractmethod
    def __iter__(self):
        pass


class ArithmeticProgression(Progression):
    def __iter__(self):
        return cnt(self.start, self.step)


class GeometricProgression(Progression):
    def __iter__(self):
        return map(lambda x: self.start * self.step ** x, cnt())


class DomainException(Exception):
    pass


class Domain:
    def __init__(self, domain):
        if re.fullmatch(r"[a-z]+\.[a-z]+", domain):
            self.domain = domain
        else:
            raise DomainException('Недопустимый домен, url или email')

    @classmethod
    def from_url(cls, url):
        if re.fullmatch(r"https?://[a-z]+\.[a-z]+", url):
            return cls(url.split("//")[1].split("/")[0])
        else:
            raise DomainException('Недопустимый домен, url или email')

    @classmethod
    def from_email(cls, email):
        if re.fullmatch(r"[a-z]+@[a-z]+\.[a-z]+", email):
            return cls(email.split("@")[1])
        else:
            raise DomainException('Недопустимый домен, url или email')

    def __repr__(self):
        return f"{self.domain}"


class HighScoreTable:
    def __init__(self, size):
        self._table = []
        self.size = size

    @property
    def scores(self):
        return self._table[:]

    def reset(self):
        self._table.clear()

    def _fast_insert(self, score):
        for i, s in enumerate(self._table):
            if score > s:
                self._table.insert(i, score)
                break
        else:
            self._table.append(score)

    def update(self, score):
        if len(self._table) < self.size:
            self._fast_insert(score)
        elif score > self._table[-1]:
            self._table.pop()
            self._fast_insert(score)


class Pagination:
    def __init__(self, items, page_size):
        self.items = items
        self.page_size = page_size
        self._page = 1

    def get_visible_items(self):
        return self.items[(self._page - 1) * self.page_size: self._page * self.page_size]

    def prev_page(self):
        return self.go_to_page(self._page - 1)

    def next_page(self):
        return self.go_to_page(self._page + 1)

    def first_page(self):
        return self.go_to_page(1)

    def last_page(self):
        return self.go_to_page(self.total_pages)

    def go_to_page(self, page):
        if 1 <= page <= self.total_pages:
            self._page = page
        elif page < 1:
            self._page = 1
        elif page > self.total_pages:
            self._page = self.total_pages
        return self

    @property
    def total_pages(self):
        return (len(self.items) - 1) // self.page_size + 1

    @property
    def current_page(self):
        return self._page


@dataclass
class Testpaper:
    topic: str
    scheme: list[str]
    limit: str


class Student:
    def __init__(self):
        self.tests = {}

    def take_test(self, test: Testpaper, answers: list[str]):
        result = sum(a == b for a, b in zip(test.scheme, answers)) / len(test.scheme)
        result_pr = round(result * 100)
        result_text = ('Failed!', 'Passed!')[result_pr >= int(test.limit[:-1])]
        self.tests.update({test.topic: f'{result_text} ({result_pr}%)'})

    @property
    def tests_taken(self):
        if self.tests:
            return self.tests
        else:
            return "No tests taken"


class TicTacToe:
    tic_tacs = ['X', 'O']

    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = 0

    def mark(self, row, col):
        if not self.winner():
            if self.board[row - 1][col - 1] == " ":
                self.board[row - 1][col - 1] = self.tic_tacs[self.current_player]
                self.current_player = 1 - self.current_player
            else:
                print('Недоступная клетка')
        else:
            print('Игра окончена')

    def show(self):
        print('\n-----\n'.join(['|'.join(row) for row in self.board]))

    def winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][0]
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]
        if not " " in [x for row in self.board for x in row]:
            return "Ничья"
        return None


class Cell:
    def __init__(self, row, col, mine=False):
        self.row = row
        self.col = col
        self.mine = mine
        self.neighbours = 0

    def __repr__(self):
        if self.mine:
            return '*'
        else:
            return str(self.neighbours)


class Game:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[Cell(y, x) for x in range(cols)] for y in range(rows)]
        self.set_mines()

    def set_mines(self):
        mines = self.mines
        while mines:
            x = randrange(0, self.cols)
            y = randrange(0, self.rows)
            if not self.board[y][x].mine:
                self.board[y][x].mine = True
                mines -= 1
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i or j:
                            if 0 <= y + i < self.rows and 0 <= x + j < self.cols:
                                self.board[y + i][x + j].neighbours += 1


class Selfie:
    def __init__(self):
        self._states = []

    def save_state(self):
        state = {i[0]: deepcopy(i[1]) for i in self.__dict__.items()}
        self._states.append(state)

    def recover_state(self, idx):
        if 0 <= idx < len(self._states):
            new_selfie = Selfie()
            for i in self._states[idx]:
                setattr(new_selfie, i, self._states[idx][i])
            return new_selfie
        else:
            return self


    def n_states(self):
        return len(self._states)

class MultiKeyDict(UserDict):
    def __init__(self, *args, **kwargs):
        self._aliases = {}
        super().__init__(*args, **kwargs)

    def alias(self, key, alias):
        self._aliases[alias] = key

    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return self.data[self._aliases[key]]

    def __setitem__(self, key, value):
        if key in self._aliases:
            self.data[self._aliases[key]] = value
        else:
            self.data[key] = value

    def __delitem__(self, key):
        if key in self._aliases.values():
            value = self.data[key]
            aliases = [k for k, v in self._aliases.items() if v == key]
            for alias in aliases[1:]:
                self._aliases[alias] = aliases[0]
            if aliases[0] not in self.data:
                del self._aliases[aliases[0]]
                self.data[aliases[0]] = value
        del self.data[key]

class predicate:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        value = self.func(*args, **kwargs)
        return value

    def __or__(self, other):
        if isinstance(other, self.__class__):
            return predicate(lambda *args, **kwargs: self(*args, **kwargs) or other(*args, **kwargs))
        else:
            return NotImplemented

    def __and__(self, other):
        if isinstance(other, self.__class__):
            return predicate(lambda *args, **kwargs: self(*args, **kwargs) and other(*args, **kwargs))
        else:
            return NotImplemented

    def __invert__(self):
        return predicate(lambda *args, **kwargs: not self(*args, **kwargs))