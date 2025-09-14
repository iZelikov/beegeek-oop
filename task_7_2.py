class BasicPlan:
    can_stream = True
    can_download = True
    has_SD = True
    has_HD = False
    has_UHD = False
    num_of_devices = 1
    price = "8.99$"


class SilverPlan(BasicPlan):
    has_HD = True
    num_of_devices = 2
    price = "12.99$"


class GoldPlan(BasicPlan):
    has_HD = True
    has_UHD = True
    num_of_devices = 4
    price = "15.99$"


class WeatherWarning:
    def rain(self):
        print("Ожидаются сильные дожди и ливни с грозой")

    def snow(self):
        print("Ожидается снег и усиление ветра")

    def low_temperature(self):
        print("Ожидается сильное понижение температуры")


import datetime


class WeatherWarningWithDate(WeatherWarning):
    def rain(self, d: datetime.date):
        print(d.strftime("%d.%m.%Y"))
        super().rain()

    def snow(self, d: datetime.date):
        print(d.strftime("%d.%m.%Y"))
        super().snow()

    def low_temperature(self, d: datetime.date):
        print(d.strftime("%d.%m.%Y"))
        super().low_temperature()


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)


class Counter:
    def __init__(self, start: int = 0):
        self.value = start

    def inc(self, number: int = 1):
        self.value += number

    def dec(self, number: int = 1):
        self.value = max(self.value - number, 0)


class DoubledCounter(Counter):
    def inc(self, number: int = 1):
        super().inc(2 * number)

    def dec(self, number: int = 1):
        super().dec(2 * number)


class Summator:
    def total(self, n, m=1):
        return sum(i ** m for i in range(1, n + 1))


class SquareSummator(Summator):
    def total(self, n, m=2):
        return super().total(n, m)


class QubeSummator(Summator):
    def total(self, n, m=3):
        return super().total(n, m)


class CustomSummator(Summator):
    def __init__(self, m):
        self.m = m

    def total(self, n, m=1):
        m = self.m
        return super().total(n, m)


class FieldTracker:
    def __init__(self):
        for attr in self.fields:
            self.__dict__[f"_base_{attr}"] = self.__dict__[attr]

    def base(self, name):
        return self.__dict__.get(f"_base_{name}")

    def has_changed(self, name):
        return self.base(name) != self.__dict__.get(name)

    def changed(self):
        return {attr: self.base(attr) for attr in self.fields if self.has_changed(attr)}

    def save(self):
        FieldTracker.__init__(self)
