class GeometricShape:
    def __init__(self, color = 'Black', filled = False):
        self.__color = color
        self.__filled = filled
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color
    def is_filled(self):
        return self.__filled
    def set_filled(self, filled):
        self.__filled = filled
    def __str__(self):
        return f'Color: {self.__color} Filled: {self.__filled}'
class Circle(GeometricShape):
    def __init__(self, color = 'Yellow', filled = False, radius = 1):
        super().__init__(color, filled)
        self.__radius = radius
    def get_radius(self):
        return self.__radius
    def set_radius(self, radius):
        self.__radius = radius
    def __str__(self):
        return 'Circle: \n' + super().__str__() + f' Radius: {self.__radius}'

class Rectangle(GeometricShape):
    def __init__(self, width = 10, height = 10, color = 'Red', filled = False):
        super().__init__(color, filled)
        self.__width = width
        self.__height = height
    def get_width(self):
        return self.__width
    def set_width(self, width):
        self.__width = width
    def get_height(self):
        return self.__height
    def set_height(self, height):
        self.__height = height
    def __str__(self):
        return 'Rectangle: \n' + super().__str__() + f' Width: {self.__width}' + f' Height: {self.__height}'