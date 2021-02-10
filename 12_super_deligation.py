
# Чаще всего super() используется для наследования __init__  метода класс Родителя 
# Для соблюдения принципа Dry

class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, surname):
        # Функция super ищет определение метода не только в родительском классе
        # но и по всему дереву наследования + порядок в которм мы вызыаем функцию super имеет значение
        super().__init__(name)
        self.surname = surname


class Person1:
    def hello(self):
        print(f'Bound with {self}')

class Student1(Person1):
    def hello(self):
        print('Student obj.hello() is called')
        super().hello()

s = Student1()

# Метод super все равно будет связан с классом Student1
s.hello()

    
    
