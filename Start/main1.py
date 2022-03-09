
# inheritance



# class Car:
#     type = ""
#
#     def carrying(self):
#         print("3.5 tons")
#
#
# class Passenger(Car):
#
#     def __init__(self, type):
#         self.type = type
#
#     def carrying(self):              #polimorphizm
#         print("less then 3.5 tons")



# car = Passenger(type = "universal")
# print(car.type)
# car.carrying()

#encapsulation

# class Info:
#     type = ""
#     color = ""
#     __code = 0
#
#     def __init__(self, type, color, code):
#         self.type = type
#         self.color = color
#         self.__code = code
#
#     def Get_code(self):
#         return self.__code
#
# count = 0
# count += 1
# car = Info("universal", "white", count)
#
# print(car.Get_code())

# Ромб

class Rhombus:
    __diag1 = 0
    __diag2 = 0


    def __init__(self, diag1, diag2):
        self.__diag1 = diag1
        self.__diag2 = diag2

    @property
    def area(self):
        return self.__diag1 / 2 + self.__diag2 / 2

    def resize(self, diag1, diag2):
        self.__diag1 = diag1
        self.__diag2 = diag2


r1 = Rhombus(2,6)
print(r1.area)
r1.resize(3,8)
print(r1.area)










