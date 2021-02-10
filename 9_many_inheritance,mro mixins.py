# множественные наследования

class Person:
    def hello(self):
        return ('Hello from Person')

class Student(Person):
    def hello(self):
        return ('Hello from Student')

class Prof(Person):
    def hello(self):
        return ('Hello from Prof')

class SomeOne(Student, Prof):
    pass

s = SomeOne()

# В каком порядке будет происходить наследование?
print('Наследование происходит с лево на право')
print(s.hello())
print('Что бы посмотеть порядок наследования используй s.__class__.mro()')
print(s.__class__.mro())

# MIXINS
class FoodMixin:
    food = None

    def get_food(self):
        if self.food is None:
            raise ValueError('Food should be set')
        print(f'I like { self.food }')

class Human:
    def hello(self):
        print('hello from Human')
    
class Driver(FoodMixin ,Human):
    food = 'bread'

    def hello(self):
        print('hello from Driver')

d = Driver()

d.hello()
d.get_food()
