
# inheritance
import code


class Car:
    type = ""

    def carrying(self):
        print("3.5 tons")


class Passenger(Car):

    def __init__(self, type):
        self.type = type

    def carrying(self):              #polimorphizm
        print("less then 3.5 tons")



 car = Passenger(type = "universal")
 print(car.type)
 car.carrying()

#encapsulation

class Info:
    type = ""
    color = ""
    __code = 0

    def __init__(self, type, color, code):
        self.type = type
        self.color = color
        self.__code = code

    def Get_code(self):
        return self.__code

count = 0
count += 1
car = Info("universal", "white", count)

print(car.Get_code())




