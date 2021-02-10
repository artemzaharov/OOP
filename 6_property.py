# свойства класса(properties) это способ доступа к переменным класса(атрибутам класса)
# обращаемся к переменным класса(атрибутам класса) что бы прочитать/поменять их

class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('From get_name()')
        return self._name

    def set_name(self, value):
        print('From set_name()')
        self._name = value

    name = property(fget=get_name, fset=set_name)


p = Person('Dima')


class Person1:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('From get_name()')
        return self._name

    def set_name(self, value):
        print('From set_name()')
        self._name = value

    name = property()
    name = name.getter(get_name)
    name = name.setter(set_name)


class Person2:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('From get_name()')
        return self._name

    def set_name(self, value):
        print('From set_name()')
        self._name = value

    name = property(get_name)
    name = name.setter(set_name)


class Person3:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name
    # получает на вход функцию name
    name = property(name)


class Person4:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    name = name.setter(set_name)


class Person5:
    def __init__(self, name):
        self._name = name

    # две функции с одинаковыми именами но у них разные декораторы
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
