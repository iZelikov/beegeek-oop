from datetime import date
from enum import Enum, IntEnum


class HTTPStatusCodes(Enum):
    CONTINUE = 100
    OK = 200
    USE_PROXY = 305
    NOT_FOUND = 404
    BAD_GATEWAY = 502

    def info(self):
        return self.name, self.value

    def code_class(self):
        code_classes = {
            1: "информация",
            2: "успех",
            3: "перенаправление",
            4: "ошибка клиента",
            5: "ошибка сервера"}
        return code_classes[self.value // 100]


class Seasons(Enum):
    WINTER = 1
    SPRING = 2
    SUMMER = 3
    FALL = 4

    def text_value(self, country_code):
        seasons = {
            "ru": Enum("RuSeasons", ["зима", "весна", "лето", "осень"]),
            "en": Enum("EnSeasons", ["winter", "spring", "summer", "fall"]),
        }
        return seasons[country_code](self.value).name


class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class NextDate:
    def __init__(self, today: date, weekday: Weekday, considering_today: bool = False):
        n = int(not considering_today)
        d = today.toordinal()
        while date.fromordinal(d + n).weekday() != weekday.value:
            n += 1
        self._date = date.fromordinal(d + n)
        self._days_until = n

    def date(self):
        return self._date

    def days_until(self):
        return self._days_until
