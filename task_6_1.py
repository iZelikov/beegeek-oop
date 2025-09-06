class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.z})"

    def __iter__(self):
        return iter((self.x, self.y, self.z))

class DevelopmentTeam:
    def __init__(self):
        self.juniors = []
        self.seniors = []
    def add_junior(self, *args):
        self.juniors += args

    def add_senior(self, *args):
        self.seniors += args

    def __iter__(self):
        from itertools import repeat
        yield from zip(self.juniors, repeat('junior'))
        yield from zip(self.seniors, repeat('senior'))

class AttrsIterator:
    def __init__(self, obj):
        self.iter = iter(obj.__dict__.items())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iter)


class SkipIterator:
    def __init__(self, iterable, n: int):
        from itertools import islice
        self.iter = islice(iterable, 0, None, n + 1)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iter)


class RandomLooper:
    def __init__(self, *args):
        from random import shuffle
        collection = sum(map(list, args), [])
        shuffle(collection)
        self.iter = iter(collection)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iter)

class Peekable:
    def __init__(self, iterable):
        self.iterable = list(iterable)
        self.iterator = iter(self.iterable)
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.counter +=1
        return next(self.iterator)

    def peek(self, default = "lmkjdsjmcvfio8sjnlkw34kjnv9lk,msdoj908"):
        try:
            return self.iterable[self.counter]
        except:
            if default != "lmkjdsjmcvfio8sjnlkw34kjnv9lk,msdoj908":
                return default
            else:
                raise StopIteration

class LoopTracker:
    def __init__(self, iterable):
        self._iter = iter(iterable)
        self._accesses = 0
        self._empty_accesses = 0
        self._first = []
        self._last = []
        self._cache = []

    @property
    def accesses(self):
        return self._accesses

    @property
    def empty_accesses(self):
        return self._empty_accesses

    @property
    def first(self):
        if not self._first:
            try:
                first = next(self._iter)
                self._first.append(first)
                self._cache.append(first)
            except:
                raise AttributeError("Исходный итерируемый объект пуст")
        return self._first[0]

    @property
    def last(self):
        try:
            return self._last[0]
        except:
            raise AttributeError('Последнего элемента нет')

    def is_empty(self):
        if self._cache:
            return False
        else:
            try:
                nxt = next(self._iter)
                self._cache.append(nxt)
                return False
            except:
                return True

    def __iter__(self):
        return self

    def __next__(self):
        if self._cache:
            nxt = self._cache.pop()
        else:
            try:
                nxt = next(self._iter)
            except StopIteration:
                self._empty_accesses +=1
                raise StopIteration
        if not self._first:
            self._first.append(nxt)

        if self._last:
            self._last[0] = nxt
        else:
            self._last.append(nxt)
        self._accesses +=1
        return nxt
