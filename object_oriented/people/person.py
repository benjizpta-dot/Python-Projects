    
class Person:

    def __init__(self, name = 'Josh', age = 20, height = "5,8", weight = 160):
        self.__name = name
        self.__age = age
        self.__height = height
        self.__weight = weight
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_height(self):
        return self.__height
    def get_weight(self):
        return self.__weight
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age
    def set_height(self, height):
        self.__height = height
    def set_weight(self, weight):
        self.__weight = weight
    def __str__(self):
        return f'Name: {self.__name} Age: {self.__age} Height: {self.__height} Weight: {self.__weight}'

class Student(Person):

    def __init__(self, ID = '123456', name = 'Josh', age = 20, height = "5,8", weight = 160, major = 'Computer Science', GPA = 4.0):
        
        super().__init__(name, age, height, weight)
        self.__ID = ID
        self.__major = major
        self.__GPA = GPA  
    def get_ID(self):
        return self.__ID
    def set_ID(self, ID):
        self.__ID = ID
    def get_major(self):
        return self.__major
    def set_major(self, major):
        self.__major = major
    def get_GPA(self):
        return self.__GPA
    def set_GPA(self, GPA):
        self.__GPA = GPA
    def __str__(self):
            return f'Student: {super().__str__()} ID: = {(self.__ID)} Major: = {self.__major} GPA: = {self.__GPA} '

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.__ID == other.__ID
