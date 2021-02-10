from weakref import WeakKeyDictionary
import weakref


class Person:
    pass


p = Person()

# Создали объект слабой ссылки которая ссылается на объект Person по адресу
w = weakref.ref(p)
print(w)
# Проверим id объекта p
print(hex(id(p)))
# Проверим p
print(p)

del p

# Ссылка стало мертвой но осталась как объект в памяти
print(w)

# Слабая ссылка является вызываемым объектом при вызове она возвращает объект на который ссылается
n = Person()
r = weakref.ref(n)
print(r())

# Если во время вызова слабой ссылки оригинальный объект будет мертв то Python вернет None
del n
print(r())

# Для реализации хранения данных в дескрипторе мы можем использовать словарь слабых ссылок
z = Person()
d = weakref.WeakKeyDictionary()
print(d)

# И теперь если я передам экземпляр класса в качестве ключа к словаря d и присвою ему значение
# то Питон автоматически создаст слабую ссылку на объект класса Person
d[z] = 10

# Вот его значение
print(d[z])

# А вот его методы
print(dir(d))

# Посмотреть все ссылки с помощью
print(d.keyrefs())
del z

# Если удалить объект, вернет пустой список
print(d.keyrefs())

# Для того что бы объект мог быть ключем словаря он должен быть хэшируемым
# То есть у него дложны быть определены методы __hash__ и __eq__

p1 = Person()
print('Hash of p1:', hash(p1))

# Если мы переопределим метод __eq__ классе Person то объкты больше не смогут быть ключем словаря


class Person2:
    def __init__(self, name):
        self.name = name

    def __eq__(self, obj):
        return isinstance(obj, Person2) and self.name == obj.name


f = Person2('Artem')
d1 = {}

# Больше не хешируемый
'''hash(f)'''
# Не сможет быть ключем словаря
'''d1[f] = 1'''

# Правильная реализация выглядит так:


class Person3:
    def __init__(self, name):
        self.name = name

    def __eq__(self, obj):
        return isinstance(obj, Person3) and self.name == obj.name

    def __hash__(self):
        return hash(self.name)


l = Person3('Artem!!!')

# Теперь объект l стал хешируемый и мы можем использовать его
print('Hash of l:', hash(l))

# Пример из прошлого видео но с weakref.WeakKeyDictionary()
class IntDescriptor:
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __set__(self, instance, value):
        self._values[instance] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._values.get(instance)


class Vector:
    x = IntDescriptor()
    y = IntDescriptor()


v = Vector()
print(hex(id(v)))

v.x = 10
# Посмотрим список слабых ссылок на объекты
print(Vector.x._values.keyrefs())

del v
print(Vector.x._values.keyrefs())