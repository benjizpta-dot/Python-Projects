import math

class GeometricShape:
    def __init__(self, color =
             "green", filled = True):
         self.__color = color # Set color
         self.__filled = filled
    def get_color(self):
         return self.__color # Get color
    def set_color(self, color):
            self.__color = color
    def is_filled(self):
            return self.__filled
    def set_filled(self, filled):
         self.__filled = filled
    def __str__(self):
        return f'Shape Attributes: Color={self.__color}\
\t Filled={str(self.__filled)}'

class Circle(GeometricShape): 

    def __init__(self, radius=1): 
        super().__init__() # Invoke superclass's init method
                           # to initialize color and filled
        self.__radius = radius # Set radius
    def get_radius(self):
        return self.__radius
    def set_radius(self, radius):
        self.__radius = radius
    def get_area(self):
        return self.__radius * self.__radius * math.pi
    def get_perimeter(self):
        return 2 * self.__radius * math.pi

    def __str__(self):
        return f'Circle: {super().__str__()} Radius={str(self.__radius)}'
    
class Rectangle(GeometricShape):
    def __init__(self, width = 1, height = 1):
        super().__init__() # Invoke base class init method
        self.__width = width # Initialize width & height
        self.__height = height
    def get_width(self):
        return self.__width
    def set_width(self, width):
        self.__width = width
    def get_height(self):
        return self.__height
    def set_height(self, height):
        self.__height = height
    def get_area(self):
        return self.__width * self.__height
    def get_perimeter(self):
        return 2 * (self.__width + self.__height)
# Override the __str__ method defined in base class
   # Override the __str__ method defined in base class
    def __str__(self):
        return f'Rectangle: {super().__str__()} Width={str(self.__width)} Height= {self.__height}'
