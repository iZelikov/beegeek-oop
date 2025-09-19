# class A:
#     pass
#
#
# class B(A):
#     pass
#
#
# class C(A):
#     pass
#
#
# class D(A):
#     pass
#
#
# class E(B, D):
#     pass


class H:
    pass


class D(H):
    pass


class E(H):
    pass


class F(H):
    pass


class G(H):
    pass


class B(D, E):
    pass


class C(F, G):
    pass


class A(B, C):
    pass


def get_method_owner(cls, method):
    for c in cls.__mro__:
        if method in c.__dict__:
            return c
    return None


class Human:
    def __init__(self, mood='neutral'):
        self.mood = mood


class Father(Human):
    def be_strict(self):
        self.mood = 'strict'

    def greet(self):
        return "Hello!"


class Mother(Human):
    def greet(self):
        return "Hi, honey!"

    def be_kind(self):
        self.mood = 'kind'


class Son(Father, Mother):
    pass


class Daughter(Mother, Father):
    pass


class MROHelper:
    @staticmethod
    def len(cls):
        return len(cls.__mro__)

    @staticmethod
    def class_by_index(cls, n=0):
        return cls.__mro__[n]

    @staticmethod
    def index_by_class(child, parent):
        return child.__mro__.index(parent)
