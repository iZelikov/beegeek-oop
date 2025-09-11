import sys
import time
from copy import deepcopy, copy


class SuppressAll:
    def __enter__(self):
        return

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True


class Greeter:
    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        print(f"Приветствую, {self.name}!")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"До встречи, {self.name}!")
        return True


class Closer:
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(self.obj, 'close'):
            self.obj.close()
        else:
            print("Незакрываемый объект")
        return True


class ReadableTextFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r', encoding='UTF-8')
        return map(lambda x: x.rstrip('\n'), self.file)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True


class Reloopable:
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True

    def __iter__(self):
        self.file.seek(0)
        return self.file


class UpperPrint:
    def __enter__(self):
        self.write = sys.stdout.write
        sys.stdout.write = lambda s: self.write(s.upper())

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write = self.write
        return True


class Suppress:
    def __init__(self, *args):
        self.exceptions = args
        self.exception = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.exceptions:
            self.exception = exc_val
            return True
        return False


class WriteSpy:
    def __init__(self, file1, file2, to_close=False):
        self.file1 = file1
        self.file2 = file2
        self.to_close = to_close

    def write(self, text):
        try:
            self.file1.write(text)
            self.file2.write(text)
        except:
            raise ValueError('Файл закрыт или недоступен для записи')

    def close(self):
        self.file1.close()
        self.file2.close()

    def writable(self):
        if (not self.file1.closed) and (not self.file2.closed):
            return self.file1.writable() and self.file2.writable()
        return False

    def closed(self):
        return self.file1.closed and self.file2.closed

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.to_close:
            self.close()
        return False


class Atomic:
    def __init__(self, data, deep: bool = False):
        self.data = data
        self.deep = deep

    def __enter__(self):
        self.backup = deepcopy(self.data) if self.deep else copy(self.data)
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.data.clear()
            if isinstance(self.data, list):
                self.data += self.backup
            else:
                self.data |= self.backup
        return True


class AdvancedTimer:
    def __init__(self):
        self.runs = []

    @property
    def last_run(self):
        if self.runs:
            return self.runs[-1]
        return None

    @property
    def min(self):
        return min(self.runs, default=None)

    @property
    def max(self):
        return max(self.runs, default=None)

    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.runs.append(time.perf_counter() - self.start)


class HtmlTag:
    indent = "  "
    level = 0

    def __init__(self, tag, inline=False):
        self.tag = tag
        self.inline = inline

    def print(self, content):
        indent = self.__class__.level * self.__class__.indent
        if self.inline:
            print(content, end="")
        else:
            print(f"{indent}{content}")

    def __enter__(self):
        indent = self.__class__.level * self.__class__.indent
        if self.inline:
            print(f"{indent}<{self.tag}>", end="")
        else:
            print(f"{indent}<{self.tag}>")
        self.__class__.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__class__.level -= 1
        indent = self.__class__.level * self.__class__.indent
        if self.inline:
            print(f"</{self.tag}>")
        else:
            print(f"{indent}</{self.tag}>")


class Node:
    def __init__(self):
        self.parent = None
        self.children = []

    def get_items(self):
        result = []
        for item in self.children:
            if isinstance(item, Node):
                if item.children:
                    result.append(item.get_items())
            else:
                result.append(item)
        return result

class TreeBuilder:
    def __init__(self):
        self.root: Node = Node()
        self.current: Node = self.root

    def add(self, item):
        self.current.children.append(item)

    def structure(self):
        return self.root.get_items()

    def __enter__(self):
        children_node = Node()
        self.current.children.append(children_node)
        children_node.parent = self.current
        self.current = children_node

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.current = self.current.parent
        return True