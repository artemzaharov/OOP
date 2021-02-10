class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        # кэшируем фулнэйм, если будут задействованы сеттеры def surname(self, value): или def name(self, value):
        # в остальных случаях отдаем имя из кэша, то есть не вычесляем его
        self._full_name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self._full_name = None

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value
        self._full_name = None

    # вычисляемое свойство(Сможем всегда получать актуальную имя и фамилию)
    @property
    def full_name(self):
        if self._full_name is None:    
            self._full_name = f'{self._name} {self._surname}'
        return self._full_name
    
    
p = Person('Artem', 'Zakharov')
