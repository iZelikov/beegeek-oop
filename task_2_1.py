from typing import Sequence


def darts():
    n = int(input())
    [print(*(min(i, j, n - i + 1, n - j + 1) for j in range(1, n + 1))) for i in range(1, n + 1)]


def skobki():
    import re
    seq, n = input(), 1
    pattern = re.compile(r'(\([^()]*\))')
    while n:
        seq, n = pattern.subn('', seq)
    print(not bool(re.search(r'[()]', seq)))


def inversions(s: Sequence[int]) -> int:
    return sum(sum(map(lambda x: x < n, s[i + 1:])) for i, n in enumerate(s))


def jsonify(func):
    import json
    from functools import wraps
    @wraps(func)
    def inner(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))

    return inner


def is_coordinate():
    import re
    coords = [map(float, re.findall(r'-?\d+\.\d+|-?\d+', line)) for line in open(0).readlines()]
    for x, y in coords:
        print(-90 <= x <= 90 and -180 <= y <= 180)


def quantify(iterable, predicate) -> int:
    return sum(map(predicate or bool, iterable))


def pycon():
    global calendar
    from calendar import monthcalendar
    from datetime import date, timedelta
    year, month = int(input()), int(input())
    calendar = monthcalendar(year, month)
    days = calendar[3][3] + 7 * (not bool(calendar[0][3])) - 1
    d = date(year, month, 1) + timedelta(days=days)
    print(d.strftime('%d.%m.%Y'))


def is_integer(string):
    try:
        int(string)
        return True
    except:
        return False


def is_decimal(string):
    try:
        float(string)
        return True
    except:
        return False


def is_fraction(string):
    from fractions import Fraction
    try:
        int(string)
        return False
    except:
        try:
            Fraction(string)
            return True
        except:
            return False


def intersperse(iterable, delimiter):
    it = iter(iterable)
    try:
        i = next(it)
        while True:
            yield i
            i = next(it)
            yield delimiter
    except:
        return


def annual_return(start: float, percent: float, years: int):
    for _ in range(years):
        start = start * (100 + percent) / 100
        yield start


def pluck(data: dict, path: str, default=None):
    if not '.' in path:
        return data.get(path, default)
    else:
        key, path = path.split('.', 1)
        try:
            return pluck(data.get(key, default), path, default)
        except:
            return default


def recviz(func):
    from functools import wraps
    depth = -1

    @wraps(func)
    def inner(*args, **kwargs):
        nonlocal depth
        depth += 1
        intends = ' ' * 4 * depth
        print(intends, end='')
        print(f'-> {func.__name__}(', end="")
        print(*[repr(arg) for arg in args], *[f'{k}={repr(v)}' for k, v in kwargs.items()], sep=', ', end='')
        print(')')
        result = func(*args, **kwargs)
        print(intends, end='')
        print(f'<- {repr(result)}')
        depth -= 1
        return result

    return inner
