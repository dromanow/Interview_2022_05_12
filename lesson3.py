class Animal:
    def sound(self):
        print('Animal')


class Cat(Animal):
    def sound(self):
        super().sound()
        print('Cat')


class Dog(Animal):

    # def get_count(self):
    #     return self._count
    #
    # def set_count(self, value):
    #     self._count = value
    #
    count = property(fget=get_count, fset=set_count)

    def __init__(self):
        self._count = 10

    def sound(self):
        super().sound()
        print('Dog')


# class Meta(type):
#     def mro(self):
#         return [self, Cat, Dog, Animal, object]

# Animal
# Dog
# Cat
# CatDog


# CatDog, Dog, Cat, Animal

# class CatDog(Cat, Dog):
#     value = 10
#     def sound(self):
#         super().sound()
#         print('CatDog')


def sound_raw(self):
    super(CatDog, self).sound()
    print('CatDog')


def init_raw(self):
    self.value1 = 20


def get_count(self):
    return self._count


def set_count(self, value):
    self._count = value

# count = property(fget=get_count, fset=set_count)


class Meta(type):
    def __new__(cls, class_name, parent, attrs, value1):
        attrs['value1'] = value1
        mod_attr = {}
        for key, value in attrs.items():
            mod_attr[key] = value
            if not key.startswith('__'):
                mod_attr[key.upper()] = value
        return super().__new__(cls, class_name, parent, mod_attr)

    # def mro(self):
    #     return [self, Cat, Dog, Animal, object]


# CatDog = Meta('CatDog', (Cat, Dog), {'sound': sound_raw, 'value': 10, '__init__': init_raw,
#                                      'count': property(fget=get_count, fset=set_count)})


class CatDog(Cat, Dog, metaclass=Meta, value1=60):
    value = 10

    def sound(self):
        super().sound()
        print('CatDog')


class PigHorse(Cat, Dog, metaclass=Meta, value1=100):
    value = 10

    def sound(self):
        super().sound()
        print('PigHorse')


catdog = CatDog()

# catdog.sound()
catdog.SOUND()
print(catdog.value1)
# catdog.COUNT = 30

pighorse = PigHorse()

pighorse.SOUND()
print(pighorse.value1)


# # print(catdog.value)
# print(CatDog.__dict__)
# print(catdog.__dict__)
#


