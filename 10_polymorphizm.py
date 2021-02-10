# Полиморфизм в питоне относится к магическим методам
# То есть с двумя подчеркиваниями спереди и с сзади __eq__ 


class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = self.x * self.y

    def __add__(self, room_obj):
        if isinstance(room_obj, Room):
            return self.area + room_obj.area
        return TypeError('Wrong object')

    def __eq__(self, room_obj):
        if isinstance(room_obj, Room):
            if self.area == room_obj.area:
                return True
            return False

p1 = Room(3, 20)
p2 = Room(5, 4)

print(p1 + p2)
print(p1 == p2)

