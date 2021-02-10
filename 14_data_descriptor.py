from time import time

# Ниже плохой пример так как все экземрляры класса MyTime работаеют с одним дескриптором Epoch
class Epoch:
    def __get__(self, instance, owner_class):
        print(f'Self: {self}')
        print(f'Id of sels: {id(self)}')
        print(f'Instance: {instance}')
        print(f'Owner class: {owner_class}')
        if instance is None:
            return self
        return int(time())

    def __set__(self, instance, owner_class):
        pass

class MyTime:
    epoch = Epoch()

m = MyTime()
# print(m.epoch)
# print()
# print(MyTime.epoch)

class IntDescriptor:
    def __init__(self):
        self._values = {}
    
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
v.x = 5
v.y = 7
print('Создали экземпляр класса v и записали в него х и у')
print(v.x)
print(v.y)

v2 = Vector()
print('Создали экземпляр класса v2 и записали в него значения.')
v2.x = 3
v2.y = 1
print(v2.x)
print(v2.y)
# Посмотрим словарь _values is класса
print(Vector.x._values)