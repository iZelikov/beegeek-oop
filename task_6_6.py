import sys
from contextlib import contextmanager


@contextmanager
def make_tag(tag: str):
    print(tag)
    yield
    print(tag)


@contextmanager
def reversed_print():
    temp_write = sys.stdout.write
    sys.stdout.write = lambda s: temp_write(s[::-1])
    yield
    sys.stdout.write = temp_write


@contextmanager
def safe_write(filename):
    file = open(filename, 'a')
    cursor = file.tell()
    print(f"cursor - {cursor}")
    try:
        yield file
    except Exception as err:
        file.truncate(cursor)
        print('Во время записи в файл было возбуждено исключение', type(err).__name__)
    finally:
        file.close()

@contextmanager
def safe_open(filename, mode='r'):
    file = None
    try:
        file = open(filename, mode)
    except Exception as e:
        yield None, e
    else:
        yield file, None
    finally:
        if file:
            file.close()
