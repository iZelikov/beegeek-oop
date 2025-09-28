import datetime
import json


class JsonSerializableMixin:
    def to_json(self):
        return json.dumps(self.__dict__)


class LoggerMixin:
    def log(self, level: str, message: str):
        date_format = '%d.%m.%Y %H:%M:%S'
        print(f'[{datetime.datetime.now().strftime(date_format)}] - {level} - {self.__class__.__name__}: {message}')


class AttributesMixin:
    def get_public_attributes(self):
        return [item for item in self.__dict__.items() if not item[0].startswith('_')]

    def get_protected_attributes(self):
        return [item for item in self.__dict__.items() if item[0].startswith('_') and not '__' in item[0]]


class ToStringMixin:
    def __repr__(self):
        if len(self.__dict__) <= 6:
            s = "{" + ", ".join(f"{repr(k)}: {repr(v)}" for k, v in self.__dict__.items()) + '}'
        else:
            d = {k: v for k, v in list(self.__dict__.items())[:6]}
            s = "{"+ ", ".join(f"{repr(k)}: {repr(v)}" for k, v in d.items()) + ', ...}'
        return f'{self.__class__.__name__}({s})'
