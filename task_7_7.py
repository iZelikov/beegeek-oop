from datetime import date


class CommonDate:
    def __init__(self, year, month, day):
        self.date = date(year, month, day)

    def iso_format(self):
        return self.date.isoformat()


class USADate(CommonDate):
    def format(self):
        return self.date.strftime('%m-%d-%Y')


class ItalianDate(CommonDate):
    def format(self):
        return self.date.strftime('%d/%m/%Y')


class Stat:
    def __init__(self, iterable=None):
        self.items = list(iterable or [])

    def add(self, item):
        self.items.append(item)

    def clear(self):
        self.items = []


class AverageStat(Stat):
    def result(self):
        return sum(self.items) / len(self.items) if len(self.items) else None


class MinStat(Stat):
    def result(self):
        return min(self.items, default=None)


class MaxStat(Stat):
    def result(self):
        return max(self.items, default=None)


class LeftParagraph:
    def __init__(self, length: int):
        self.line_length = length
        self.paragraph = [""]

    def add(self, words):
        for word in words.split():
            if len(self.paragraph[-1]) + len(word) + 1 <= self.line_length:
                self.paragraph[-1] = (" ".join([self.paragraph[-1], word])).strip()
            else:
                self.paragraph.append(word)

    def end(self):
        for line in self.paragraph:
            print(line)
        self.paragraph = [""]


class RightParagraph(LeftParagraph):
    def end(self):
        for line in self.paragraph:
            print(line.rjust(self.line_length))
        self.paragraph = [""]
