class Circle:
    def __init__(self, radius):
        from math import pi
        self._radius = radius
        self._diameter = radius * 2
        self._area = pi * radius ** 2

    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return self._diameter

    def get_area(self):
        return self._area


class BankAccount:
    def __init__(self, balance: int = 0):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError('На счете недостаточно средств')
        self._balance -= amount

    def transfer(self, account, amount):
        self.withdraw(amount)
        account.deposit(amount)


class User:
    def __init__(self, name: str, age: int):
        self._name = self._is_correct_name(name)
        self._age = self._is_correct_age(age)

    def _is_correct_name(self, name: str):
        if name and isinstance(name, str) and name.isalpha():
            return name
        else:
            raise ValueError('Некорректное имя')

    def _is_correct_age(self, age: int):
        if type(age) == int and 0 <= age <= 110:
            return age
        else:
            raise ValueError('Некорректный возраст')

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = self._is_correct_name(name)

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = self._is_correct_age(age)
