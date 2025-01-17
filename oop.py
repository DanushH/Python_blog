# Class & Object
# 
# class Shape:
#     shape_type = "Quadrilateral"     # Class attribute

#     def __init__(self, name):
#         # Constructor
#         self.shape_name = name  # Object attribute


# square = Shape("Square")
# print(f"Shape Name: {square.shape_name}, Shape Type: {Shape.shape_type}")


# Encapsulation
# class Shape:
#     shape_type = "Quadrilateral"  # Class attribute

#     def __init__(self, name, length):
#         # Constructor
#         self.shape_name = name  # Public object attribute
#         self.shape_length = length
#         self.__area = 0  # Private object attribute

#     def set_area(self):
#         """
#         Setter method
#         Calculate the value of area
#         """
#         self.__area = self.shape_length**2

#     def get_area(self):
#         """
#         Getter method
#         Return the value of area
#         """
#         return self.__area


# square = Shape("Square", 800)
# square.set_area()

# print(f"Shape Name: {square.shape_name}, Shape Type: {Shape.shape_type}")
# print(f"Area: {square.get_area()}")


# Inheritance
# class Shape:
#     """
#     Super class
#     Inherited by Square and Rectangle sub classes
#     """

#     shape_type = "Quadrilateral"  # Class attribute

#     def __init__(self, name, length, width):
#         # Constructor
#         self.shape_name = name  # Public object attribute
#         self.shape_length = length
#         self.shape_width = width
#         self.__area = 0  # Private object attribute

#     def set_area(self):
#         """
#         Setter method
#         Calculate the value of area
#         """
#         self.__area = self.shape_length * self.shape_width

#     def get_area(self):
#         """
#         Getter method
#         Return the value of area
#         """
#         return self.__area


# class Square(Shape):
#     """
#     Sub class - extends Shape class
#     """

#     def __init__(self, name, side):
#         # Super class constructor invoke
#         super().__init__(name, side, side)


# class Rectangle(Shape):
#     """
#     Sub class - extends Shape class
#     """

#     def __init__(self, name, length, width):
#         # Super class constructor invoke
#         super().__init__(name, length, width)


# square = Square("Square", 8)
# square.set_area()
# rectangle = Rectangle("Rectangle", 10, 8)
# rectangle.set_area()

# print(f"Shape Name: {square.shape_name}, Shape Type: {Shape.shape_type}")
# print(f"Area: {square.get_area()}")
# print(f"Shape Name: {rectangle.shape_name}, Shape Type: {Shape.shape_type}")
# print(f"Area: {rectangle.get_area()}")


# Abstraction
# from abc import ABC, abstractmethod


# class Shape(ABC):  # Abstract class Shape

#     shape_type = "Quadrilateral"  # Class attribute

#     def __init__(self, name):  # Constructor
#         self.shape_name = name  # Public object attribute

#     @abstractmethod
#     def set_area(self):  # Abstract setter method
#         pass

#     @abstractmethod
#     def get_area(self):  # Abstract getter method
#         pass


# class Square(Shape):
#     """
#     Subclass Square 
#     Extends abstract class Shape
#     """

#     def __init__(self, name, side): # Constructor
#         super().__init__(name)
#         self.side = side    # Public object attribute
#         self.__area = 0     # Private object attribute

#     def set_area(self):     # Concrete setter method
#         self.__area = self.side**2

#     def get_area(self):     # Concrete getter method
#         return self.__area


# square = Square("Square", 8)
# square.set_area()

# print(f"Shape Name: {square.shape_name}, Shape Type: {Shape.shape_type}")
# print(f"Area: {square.get_area()}")


# Polymorphism
# class Rectangle(Shape):
#     """
#     Subclass Rectangle 
#     Extends abstract class Shape
#     """

#     def __init__(self, name, length, width):    # Constructor
#         super().__init__(name)
#         self.length = length    # Public object attribute
#         self.width = width      # Public object attribute
#         self.__area = 0     # Private object attribute

#     def set_area(self):     # Concrete setter method
#         self.__area = self.length * self.width

#     def get_area(self):     # Concrete getter method
#         return self.__area


# rectangle = Rectangle("Rectangle", 10, 8)
# rectangle.set_area()

# print(f"Shape Name: {rectangle.shape_name}, Shape Type: {Shape.shape_type}")
# print(f"Area: {rectangle.get_area()}")



# Complete OOP Code Example
from abc import ABC, abstractmethod


class Shape(ABC):  # Abstract class Shape

    shape_type = "Quadrilateral"  # Class attribute

    def __init__(self, name):  # Constructor
        self.shape_name = name  # Public object attribute

    @abstractmethod
    def set_area(self):  # Abstract setter method
        pass

    @abstractmethod
    def get_area(self):  # Abstract getter method
        pass


class Square(Shape):
    """
    Subclass Square
    Extends abstract class Shape
    """

    def __init__(self, name, side):  # Constructor
        super().__init__(name)
        self.side = side  # Public object attribute
        self.__area = 0  # Private object attribute

    def set_area(self):  # Concrete setter method
        self.__area = self.side**2

    def get_area(self):  # Concrete getter method
        return self.__area


class Rectangle(Shape):
    """
    Subclass Rectangle
    Extends abstract class Shape
    """

    def __init__(self, name, length, width):  # Constructor
        super().__init__(name)
        self.length = length  # Public object attribute
        self.width = width  # Public object attribute
        self.__area = 0  # Private object attribute

    def set_area(self):  # Concrete setter method
        self.__area = self.length * self.width

    def get_area(self):  # Concrete getter method
        return self.__area


square = Square("Square", 8)
square.set_area()
rectangle = Rectangle("Rectangle", 10, 8)
rectangle.set_area()

print(f"Shape Name: {square.shape_name}, Shape Type: {Shape.shape_type}")
print(f"Area: {square.get_area()}")
print(f"Shape Name: {rectangle.shape_name}, Shape Type: {Shape.shape_type}")
print(f"Area: {rectangle.get_area()}")
