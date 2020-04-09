#################### Class Method ############################################################

# defines the method getCirclesCount, bound to an object of Circle class.
class Circle(object):
    no_of_circles = 0
    def __init__(self, radius):
        self.__radius = radius
        Circle.no_of_circles += 1
    def getCirclesCount(self):
        return Circle.no_of_circles
c1 = Circle(3.5)
c2 = Circle(5.2)
c3 = Circle(4.8)
print(c1.getCirclesCount())        # --> 3
print(c2.getCirclesCount())        # --> 3
print(Circle.getCirclesCount(c3))  # --> 3
#print(Circle.getCirclesCount())    # --> TypeError: getCirclesCount() missing 1 required positional argument: 'self'


# defines the classmethod getCirclesCount, bound to class Circle.

class Circle(object):
    no_of_circles = 0
    def __init__(self, radius):
        self.__radius = radius
        Circle.no_of_circles += 1
    @classmethod
    def getCirclesCount(self):
        return Circle.no_of_circles
c1 = Circle(3.5)
c2 = Circle(5.2)
c3 = Circle(4.8)
print(c1.getCirclesCount())      # --> 3
print(c2.getCirclesCount())      # --> 3
print(Circle.getCirclesCount())  # --> 3


########################## Static Method #####################################################


# defines the method square, outside the class definition of Circle, and uses it inside the class Circle.
# def square(x):
#         return x**2
# class Circle(object):
#     def __init__(self, radius):
#         self.__radius = radius
#     def area(self):
#         return 3.14*square(self.__radius)
# c1 = Circle(3.9)
# print(c1.area())   # --> 47.7594
# print(square(10))  # --> 100


# defines the static method square, inside the class Circle, and uses it.
class Circle(object):
    def __init__(self, radius):
        self.__radius = radius
    @staticmethod
    def square(x):
        return x**2
    def area(self):
        return 3.14*self.square(self.__radius)
c1 = Circle(3.9)
print(c1.area())  
print(square(10))  # --> NameError: name 'square' is not defined