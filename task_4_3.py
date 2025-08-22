# закомментировано из-за конфликта имён
# class Gun:
#     def shoot(self):
#         print('pif')


class User:
    def __init__(self, name):
        self.name = name
        self.friends = 0

    def add_friends(self, n):
        self.friends += n


class House:
    def __init__(self, color, rooms):
        self.color = color
        self.rooms = rooms

    def paint(self, new_color):
        self.color = new_color

    def add_rooms(self, n):
        self.rooms += n


class Circle:
    def __init__(self, radius):
        from math import pi
        self.radius = radius
        self.diameter = radius * 2
        self.area = pi * radius ** 2


class Bee:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def move_up(self, n: int):
        self.y += n

    def move_down(self, n: int):
        self.move_up(-n)

    def move_right(self, n: int):
        self.x += n

    def move_left(self, n: int):
        self.move_right(-n)


class Gun:
    def __init__(self):
        import itertools
        self.sound_generator = itertools.cycle(['pif', 'paf'])
        self.shots = 0

    def shoot(self):
        self.shots += 1
        print(next(self.sound_generator))

    def shots_count(self):
        return self.shots

    def shots_reset(self):
        self.__init__()


class Scales:
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_right(self, n: int):
        self.right += n

    def add_left(self, n: int):
        self.left += n

    def get_result(self):
        return ('Левая чаша тяжелее', 'Весы в равновесии', 'Правая чаша тяжелее')[
            (self.left == self.right) - (self.left < self.right)]


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def abs(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


class Numbers:
    def __init__(self):
        self.numbers = []

    def add_number(self, n):
        self.numbers.append(n)

    def get_even(self):
        return list(filter(lambda x: not x % 2, self.numbers))

    def get_odd(self):
        return list(filter(lambda x: x % 2, self.numbers))


class TextHandler:
    def __init__(self):
        self.words = []

    def add_words(self, text: str):
        self.words += text.split()

    def get_shortest_words(self):
        return list(filter(lambda x: len(x) == len(min(self.words, key=len)), self.words))

    def get_longest_words(self):
        return list(filter(lambda x: len(x) == len(max(self.words, key=len)), self.words))


class Todo:
    def __init__(self):
        self.things = []

    def add(self, name: str, priority: int):
        self.things.append((name, priority))

    def get_by_priority(self, n: int):
        return list(map(lambda x: x[0], filter(lambda x: x[1] == n, self.things)))

    def get_low_priority(self):
        n = min(self.things, key=lambda x: x[1], default=["", -1])[1]
        return self.get_by_priority(n)

    def get_high_priority(self):
        n = max(self.things, key=lambda x: x[1], default=["", -1])[1]
        return self.get_by_priority(n)


class Postman:
    def __init__(self):
        self.delivery_data = []

    def _make_uniq(self, iterable):
        uniq_dict = dict.fromkeys(iterable)
        return list(uniq_dict)

    def add_delivery(self, street: str, house: int, flat: int):
        self.delivery_data.append((street, house, flat))

    def get_houses_for_street(self, street: str):
        return self._make_uniq(map(lambda x: x[1], filter(lambda x: x[0] == street, self.delivery_data)))

    def get_flats_for_house(self, street: str, house: int):
        return self._make_uniq(
            map(lambda x: x[2], filter(lambda x: x[0] == street and x[1] == house, self.delivery_data)))


class Wordplay:
    def __init__(self, words: list[str] = ()):
        self.words = list(words)

    def add_word(self, word: str):
        if not word in self.words:
            self.words.append(word)

    def words_with_length(self, n: int):
        return list(filter(lambda x: len(x) == n, self.words))

    def only(self, *args):
        return list(filter(lambda x: all(map(lambda c: c in args, x)), self.words))

    def avoid(self, *args):
        return list(filter(lambda x: all(map(lambda c: c not in x, args)), self.words))


class Knight:
    def __init__(self, horizontal: str, vertical: int, color: str):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color

    def _translate(self, h: int | str):
        positions = '?abcdefgh'
        if isinstance(h, str):
            return positions.find(h)
        else:
            return positions[h]

    def get_char(self):
        return 'N'

    def can_move(self, x: str, y: int):
        x = self._translate(x)
        nx, ny = self._translate(self.horizontal), self.vertical
        return (abs(nx - x) == 2 and abs(ny - y) == 1) or (abs(nx - x) == 1 and abs(ny - y) == 2)

    def move_to(self, x: str, y: int):
        if self.can_move(x, y):
            self.horizontal = x
            self.vertical = y

    def draw_board(self):
        board = [['*' if self.can_move(self._translate(x), 9 - y) else '.' for x in range(1, 9)] for y in
                 range(1, 9)]
        board[8 - self.vertical][self._translate(self.horizontal) - 1] = self.get_char()
        [print(*line, sep='') for line in board]
