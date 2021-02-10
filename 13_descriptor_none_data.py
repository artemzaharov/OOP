# class Person:
#     def __init__(self, name, surname):
#         self._name = name
#         self._surname = surname

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         self._name = value

#     @property
#     def surname(self):
#         return self._surname

#     @surname.setter
#     def surname(self, value):
#         self._surname = value

from random import choice
from time import time


class StringD:
    def __init__(self, value=None):
        if value:
            self.set(value)

    def get(self):
        return self._value

    def set(self, value):
        self._value = value


class Person:
    def __init__(self, name, surname):
        self.name = StringD(name)
        self.surname = StringD(surname)


p = Person('Artem', 'Zakharov')


class Epoch:
    def __get__(self, instance, owner_class):
        return int(time())


class MyTime:
    epoch = Epoch()


m = MyTime()


class Choice():
    def __init__(self, *choice):
        self._choice = choice

    def _get__(self, obj, owner):
        return choice(self._choice)


class Game:
    dice = Choice(range(1, 7))
    flip = Choice(['Heads', 'Tails'])
    rock_papper_scissors = Choice(['Rock', 'Papper', 'Scissors'])

# class Game:
    # @property
    # def rock_papper_scissors(self):
    #     return choice(['Rock', 'Papper', 'Scissors'])

    # @property
    # def flip(self):
    #     return choice(['Heads', 'Tails'])

    # @property
    # def dice(self):
    #     return choice(range(1, 7))


d = Game()
