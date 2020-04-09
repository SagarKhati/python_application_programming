from abc import ABC, abstractmethod
import inspect


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
#s1 = Shape()  # --> TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter
        
    
class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius
    @staticmethod
    def square(x):
        return x**2
    def area(self):
        return 3.14*self.square(self.__radius)
# c1 = Circle(3.9)  # --> TypeError: Can't instantiate abstract class Circle with abstract methods perimeter
        

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius
    @staticmethod
    def square(x):
        return x**2
    def area(self):
        return 3.14*self.square(self.__radius)
    def perimeter(self):
        return 2*3.14*self.__radius
c1 = Circle(3.9)
print(c1.area())  # --> 47.7594



##############################################################################################



# Define the abstract class 'Animal' below
# with abstract method 'say'
class Animal(ABC):
    @abstractmethod
    def say():
        pass
# Define class Dog derived from Animal
# Also define 'say' method inside 'Dog' class
class Dog(Animal):
    def say(self):
        return "I speak Booooo"
if issubclass(Animal, ABC):
    print("'Animal' is an abstract class" )
if '@abstractmethod' in inspect.getsource(Animal.say):
    print("'say' is an abstract method")    
if issubclass(Dog, Animal):
    print("'Dog' is dervied from 'Animal' class" )
d1 = Dog()
print("Dog,'d1', says :", d1.say())