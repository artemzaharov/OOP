
name = 'Ivan'


class Person:
    name = 'Dima'

    def print_name(self):
        # при таком варианте мы сиожем только прочитать свойство класса
        # а присвоить новое уже не можем потому что питон создаст такоe
        # же свойство но уже в экземпляре класса и его пространстве имен
        print(self.name)
        # а при таком варианте мы будем видеть глобальную name = 'Ivan' потому
        # что экземпляр класса находится в другом пространстве имен и обл.видимости
        '''print(name)'''


p = Person()
print(p.__dict__)
# не нашел в экземпляре класса по правилу разрешения имен идет
# в класс и то потому что есть self.name
p.print_name()
p.name = 'Arch'
print('Instance dict: ', p.__dict__)
print()
print('Person name: ', Person.name)
print()
print()

# ТО ЕСТЬ ПРИ ВАРИАНТЕ ВЫШЕ МЫ НЕ МОЖЕМ МЕНЯТЬ СВОЙСТВО КЛАССА
# ДЛЯ ТОГО ЧТО БЫ ЭТО СДЕЛАТЬ ВОСПОЛЬЗУЕМСЯ ДЕКОРАТОРОМ @classmethod
# для этого декоратора используется cls вместо self, что бы понять
# что меняем свойство класса а не экземпляра


class Persona:
    name = 'Marselle'

    @classmethod
    def change_name(cls, name):
        cls.name = name


a = Persona()
print(a.__dict__)
a.change_name('Misha')
a.name = 'Arch'
print('Instance dict: ', a.__dict__)
print()
print('Person name: ', Persona.name)
print()
print()
# САМЫЙ РАСПРОСТРАНЕННЫЙ СЛУЧАЙ ИСПОЛЬЗОВАНИЯ @classmethod 
# ЭТО АЛЬТЕРНАТИВНЫЙ ИНИЦИАЛИЗАТОР (МЫ ЖЕ НЕ МОЖЕМ ИМЕТЬ ДВА __init__ МЕТОДА)

class Human:
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def from_file(cls, path):
        with open(path) as f:
            name = f.read().strip()
        # объект класса сохранен в переменную cls
        return cls(name=name)

    @classmethod
    def from_obj(cls, obj):
        if hasattr(obj, 'name'):
            name = getattr(obj, 'name')
            return cls(name=name)
        return cls

class Armenian:

    name = 'Ara'

p = Human('Vasya')
print('Обычная инициалтзация экземпляра: ', p.name)

p = Human.from_file('text')
print('инициализация с classmethod из файла: ', p.name)

p = Human.from_obj(Armenian)
print('инициализация с classmethod из другого класса:', p.name)