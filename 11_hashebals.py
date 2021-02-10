

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    # объеты могут быть ключами словаря только при переоопредилении метода __hash__
    def __hash__(self):
        return hash(self.name)

    def __eq__(self, person_obj):
        return isinstance(person_obj, Person) and self.name == person_obj.name


p1 = Person('Ivan')
p2 = Person('artem')

print(p1 == p2)


d = {p1: 'Ivan Ivanov', p2: 'rook'}

print(d.get(p1))
