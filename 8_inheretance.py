class IntelCpu:
    cpu_socket = 1151
    name = 'Intel'


class I7(IntelCpu):
    pass


class I5(IntelCpu):
    pass


i5 = I5()

i7 = I7()

print(isinstance(i5, IntelCpu))
print(issubclass(I5, IntelCpu))
print(type(i5))

# Как узнать принадлежат ли два объекта к одному классу
print('Как узнать принадлежат ли два объекта к одному классу')
print(isinstance(i5, type(i7)))
print(issubclass(type(i5), type(i7)))

# Перегрузка методов


class Person:
    def hello(self):
        return print('Hello from Person class')


class Student(Person):
    def goodbuy(self):
        return print('Goodbuy from Student class')


s = Student()
s.hello()
print('__dict__ экземпляра', s.__dict__)
print('__dict__ класса', Student.__dict__)
s.goodbuy()

# Разрешение имен методов

class Person1:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f'hello from {self.name}')

class Students1(Person1):
    pass

st = Students1('Dima')
st.hello()
    