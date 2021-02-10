class Person:
    def hello(self):
        print('Hello')

    @staticmethod
    def goodbye():
        print('Goodbye')


a = Person()
b = Person()

'''Статический метод экономит память это один объект на все 
экземпляры, они не связаны не с экземпляром не с самим классом'''