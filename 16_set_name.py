

class ValidString:
    # вызывается в момент компиляции кода
    def __set_name__(self, owner_class, property_name ):
        self.property_name = property_name
        print(self.property_name)
        

    def __set__(self, instance, value):
        print('__set__ was called')
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be a String, but {type(value).__name__} was given!')
        # key = '_' + self.property_name
        # setattr(instance, key, value) 
        # можно использовать локальный словарь __dict__ напрямую
        instance.__dict__[self.property_name] = value
    
    def __get__(self, instance, owner):
        print('__get__ was called')
        if isinstance is None:
            return self
        # key = '_' + self.property_name
        # return getattr(instance, key, None)
        return instance.__dict__.get(self.property_name, None)


class Person:
    name = ValidString()
    surname = ValidString()
    age = ValidString()

p = Person()
