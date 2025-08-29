class ReversibleString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def __neg__(self):
        return ReversibleString(self.string[::-1])


class Money:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"{self.amount} руб."

    def __pos__(self):
        return Money(abs(self.amount))

    def __neg__(self):
        return Money(-abs(self.amount))


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __pos__(self):
        return Vector(self.x, self.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


class ColoredPoint:
    def __init__(self, x, y, color: tuple[int] = (0,0,0)):
        self.x = x
        self.y = y
        self.color = color

    def __repr__(self):
        return f"ColoredPoint({self.x}, {self.y}, {self.color})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __pos__(self):
        return self.__class__(self.x, self.y, self.color)

    def __neg__(self):
        return self.__class__(-self.x, -self.y, self.color)

    def __invert__(self):
        return self.__class__(self.y, self.x, tuple(255 - c for c in self.color))

class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self._matrix = [[value for j in range(cols)] for i in range(rows)]

    def get_value(self, row, col):
        return self._matrix[row][col]

    def set_value(self, row, col, value):
        self._matrix[row][col] = value

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"

    def __str__(self):
        return "\n".join(map(lambda x: " ".join(map(str, x)), self._matrix))

    def __pos__(self):
        new_matrix = Matrix(self.rows, self.cols)
        for row, arr in enumerate(new_matrix._matrix):
            for col, value in enumerate(arr):
                value = self.get_value(row, col)
                new_matrix.set_value(row, col, value)
        return new_matrix

    def __neg__(self):
        new_matrix = Matrix(self.rows, self.cols)
        for row, arr in enumerate(new_matrix._matrix):
            for col, value in enumerate(arr):
                value = -self.get_value(row, col)
                new_matrix.set_value(row, col, value)
        return new_matrix

    def __invert__(self):
        new_matrix = Matrix(self.cols, self.rows)
        new_matrix._matrix = list(map(list,zip(*self._matrix)))
        return new_matrix

    def __round__(self, n=None):
        new_matrix = Matrix(self.rows, self.cols)
        for row, arr in enumerate(new_matrix._matrix):
            for col, value in enumerate(arr):
                value = round(self.get_value(row, col), n)
                new_matrix.set_value(row, col, value)
        return new_matrix
