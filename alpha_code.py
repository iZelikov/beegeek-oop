from copy import copy

class N:
    def __init__(self, data):
        self.data = data
        self.copy = copy(self.data)
        self.data[6]=7
        # self.data.clear()
        # self.data |= self.copy


numbers = {1:2, 2:3, 3:4, 4:5}

n = N(numbers)
print(numbers)
