class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self.name = f'{self._name} {self._surname}'

p = Person('Artem','Zakharov')

print(p.name)