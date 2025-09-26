import functools
import json
import re


def track_instances(cls):
    cls.instances = []
    old_init = cls.__init__

    @functools.wraps(old_init)
    def new_init(self, *args, **kwargs):
        old_init(self, *args, **kwargs)
        cls.instances.append(self)

    cls.__init__ = new_init
    return cls


def add_attr_to_class(**kwargs):
    def decorator(cls):
        for k, v in kwargs.items():
            setattr(cls, k, v)
        return cls

    return decorator


def jsonattr(filename):
    with open(filename, encoding='utf-8') as f:
        data = json.load(f)

    def decorator(cls):
        for k, v in data.items():
            setattr(cls, k, v)
        return cls

    return decorator


def singleton(cls):
    instance = None

    def wrapper(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
            return instance
        else:
            cls.__init__(instance, *args, **kwargs)
            return instance

    return wrapper


def snake_case(attrs=False):
    def decorator(cls):
        d = list(cls.__dict__.items())
        for k, v in d:
            if not k.startswith('__') and (type(v).__name__ == 'function' or attrs):
                setattr(cls, re.sub(r'([^_])([A-Z])', r'\1_\2', k).lower(), v)
                delattr(cls, k)
        return cls

    return decorator


def auto_repr(args, kwargs):
    def decorator(cls):
        def __repr__(self):
            args_str = ', '.join(
                [repr(getattr(self, arg)) for arg in args] +
                [f'{k}={repr(getattr(self, k))}' for k in kwargs]
            )
            return f'{cls.__name__}({args_str})'

        cls.__repr__ = __repr__
        return cls

    return decorator


def limiter(limit: int, unique: str, lookup: str = 'FIRST'):
    instances = {}
    def decorator(cls):
        def wrapper(*args, **kwargs):
            item = cls(*args, *kwargs)
            key = getattr(item, unique)
            if key in instances:
                del item
                return instances[key]
            else:
                if len(instances) >= limit:
                    if lookup == 'LAST':
                        return list(instances.values())[-1]
                    elif lookup == 'FIRST':
                        return list(instances.values())[0]
                    else:
                        raise ValueError('lookup must be LAST or FIRST')
                else:
                    instances[key] = item
                    return item
        return wrapper
    return decorator
