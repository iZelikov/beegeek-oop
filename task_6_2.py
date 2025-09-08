from itertools import cycle


class ReversedSequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, item):
        if 0 <= item < len(self.sequence):
            return self.sequence[len(self.sequence) - item - 1]
        else:
            raise IndexError


class SparseArray:
    def __init__(self, default):
        self.default = default
        self.dict = {}

    def __getitem__(self, item):
        return self.dict.setdefault(item, self.default)

    def __setitem__(self, key, value):
        self.dict[key] = value

    def __delitem__(self, key):
        del self.dict[key]


class CyclicList:
    def __init__(self, iterable=None):
        if iterable is None:
            iterable = []
        self.list = list(iterable)
        self.iter = cycle(self.list)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iter)

    def __len__(self):
        return len(self.list)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.list[item % len(self)]
        raise TypeError

    def append(self, value):
        self.list.append(value)

    def pop(self, index=None):
        if index is None:
            return self.list.pop()
        elif isinstance(index, int):
            index = index % len(self)
            return self.list.pop(index)
        raise TypeError


class OrderedSet:
    def __init__(self, iterable=None):
        if iterable is None:
            iterable = {}
        self.d = dict.fromkeys(iterable)

    def add(self, obj):
        self.d[obj] = None

    def discard(self, obj):
        if obj in self.d:
            del self.d[obj]

    def __iter__(self):
        return iter(self.d.keys())

    def __len__(self):
        return len(self.d.keys())

    def __contains__(self, item):
        return item in self.d

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return list(self.d.keys()) == list(other.d.keys())
        elif isinstance(other, set):
            return set(self.d.keys()) == other
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, (self.__class__, set)):
            return not self.__eq__(other)
        else:
            return NotImplemented


class PermaDict:
    def __init__(self, data=None):
        self.d = {}
        self.d.update(data or {})

    def keys(self):
        return tuple(self.d.keys())

    def values(self):
        return tuple(self.d.values())

    def items(self):
        return tuple(self.d.items())

    def __len__(self):
        return len(self.d.keys())

    def __iter__(self):
        return iter(self.d.keys())

    def __getitem__(self, key):
        return self.d[key]

    def __setitem__(self, key, value):
        if key in self.d and self.d[key] != value:
            raise KeyError('Изменение значения по ключу невозможно')
        else:
            self.d[key] = value

    def __delitem__(self, key):
        if key in self.d:
            del self.d[key]


class HistoryDict:
    def __init__(self, data=None):
        if data is None:
            data = {}
        self.hd = {k: [v] for k, v in data.items()}

    def keys(self):
        return self.hd.keys()

    def values(self):
        return [item[-1] for item in self.hd.values()]

    def items(self):
        return [(k, v[-1]) for k, v in self.hd.items()]

    def history(self, key):
        return self.hd.get(key, [])

    def all_history(self):
        return self.hd

    def __len__(self):
        return len(self.hd.keys())

    def __iter__(self):
        return iter(self.hd.keys())

    def __getitem__(self, key):
        return self.hd[key][-1]

    def __setitem__(self, key, value):
        self.hd.setdefault(key, []).append(value)

    def __delitem__(self, key):
        del self.hd[key]


class Grouper:
    def __init__(self, iterable, key):
        self.d = {}
        self.key = key
        for item in iterable:
            self.add(item)

    def add(self, item):
        self.d.setdefault(self.group_for(item), []).append(item)

    def group_for(self, item):
        return self.key(item)

    def __len__(self):
        return len(self.d.keys())

    def __iter__(self):
        return iter(self.d.items())

    def __contains__(self, key):
        return key in self.d

    def __getitem__(self, key):
        return self.d[key]


class SequenceZip:
    def __init__(self, *args):
        from copy import copy
        self.data = [copy(item) for item in args]

    def __len__(self):
        return len(min(self.data, key=len, default=[]))

    def __iter__(self):
        return zip(*self.data)

    def __getitem__(self, key):
        return tuple([item[key] for item in self.data])


class MutableString:
    def __init__(self, string = None):
        self.string = list(string or "")

    def lower(self):
        self.string = list(map(str.lower, self.string))

    def upper(self):
        self.string = list(map(str.upper, self.string))

    @classmethod
    def _from_list(cls, l):
        item =  cls("")
        item.string += list(map(str, l))
        return item

    def __str__(self):
        return "".join(self.string)

    def __repr__(self):
        return f"MutableString('{str(self)}')"

    def __len__(self):
        return len(self.string)

    def __iter__(self):
        return iter(self.string)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return self._from_list(self.string[key])
        else:
            return self.__class__(self.string[key])

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            self.string[key] = list(value)
        elif isinstance(key, int):
            self.string[slice(key, (key + 1) or None)] = list(value)
        else:
            raise TypeError

    def __delitem__(self, key):
        del self.string[key]

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self._from_list(self.string + other.string)
        return NotImplemented
