import os
from abc import ABC, abstractmethod

# object
# Animal
# Cat
# a

class A:
    a = 10

    def __init__(self, c):
        self.a = self.a
        self.c = c

    def test(self):
        print('test')

    def _test(self):
        self.__test()
        print('_test')

    def __test(self):
        print('__test')

# print('class', A.__dict__)
# a = A(30)
# print('self', a.__dict__)

# getattr(a, 'test')()

# a.test()
# a.test = lambda: print('lambda')
# A.test = lambda s: print('lambda')
# print('class', A.__dict__)
# print('self', a.__dict__)

# a.test()
# a._test()
# # print('class', A.__dict__)
# a._A__test()
#
# # print(a.test)
# a.test()
#
# b = A(19)
# b.test()
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         raise NotImplementedError
#         # pass
#
#      Animal
# Cat          Dog
#      CatDog


class Animal:
    def sound(self):
        print('Animal')


class ProtoCat(Animal):
    def sound(self):
        super().sound()
        print('ProtoCat')


class Cat(ProtoCat):
    def sound(self):
        super().sound()
        print('Cat')


class Dog(Animal):
    def sound(self):
        super().sound()
        print('Dog')


class Meta(type):
    def mro(self):
        return [self, Cat, Dog, Animal, object]

# Animal
# Dog
# Cat
# CatDog


# CatDog, Dog, Cat, Animal

class CatDog(Cat, Dog, metaclass=Meta):
    def sound(self):
        super().sound()
        print('CatDog')


def sound(a: Animal):
    a.sound()


c = CatDog()
c.sound()

# print('----')
# d = Dog()
# d.sound()
#
# sound(c)
# sound(d)
#
# sound(1)


# /test
# /test/subtest.txt

def print_directory_contents(path):
    for p in os.listdir(path):
        print(p)
        x = os.path.join(path, p)
        if os.path.isdir(x):
            print_directory_contents(x)
