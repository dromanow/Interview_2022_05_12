class NonNegative:
    # def __init__(self, name):
    #     self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Order:
    price = NonNegative()
    count = NonNegative()

    def __init__(self, price, count):
        self.price = price
        self.count = count

    def get_total(self):
        return self.price * self.count

# class Order:
#     def __init__(self, price, count):
#         self._price = price
#         self._count = count
#
#     def get_count(self):
#         return self._count
#
#     def set_count(self, value):
#         if value < 0:
#             raise ValueError
#         self._count = value
#
#     count = property(fget=get_count, fset=set_count)
#
#     @property
#     def price(self):
#         return self._price
#
#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError
#         self._price = value
#
#     def get_total(self):
#         return self.price * self._count


apple = Order(10, 5)
orange = Order(12, 3)

# print(Order.__dict__)
# print(apple.__dict__)

# apple.count = -10
# apple.price = -5

# apple.set_count(-10)

print(apple.get_total())
print(orange.get_total())

print(Order.__dict__)
print(apple.__dict__)

