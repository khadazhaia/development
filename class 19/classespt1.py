from datetime import datetime
import datetime

'''
Classes
'''
# Class Definition and Initializer (camel case- first letter in each word is capatalized)
class Point2d:
    """ Initializer"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    """ String Representation"""
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    # Add your object to another object of your class
    def __add__(self, other):
        return Point2d(self.x + other.x, self.y + other.y)
    
    # Subtract my object from another object
    def __sub__(self, other):
        return Point2d(self.x - other.x, self.y - other.y)
    
    # Test equlaity between this object and another
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False
    
    # Less than function
    def __lt__(self, other):
        if self.x < other.x and self.y < other.y:
            return True
        return False
    
    # Mutator Method - Setter
    # Mutator method for x
    def set_x(self, new_x):
        self.x = new_x

    # Mutator method for y
    def set_y(self, new_y):
        self.y = new_y
    
    # Accessor method
    # Accessor method for x (outputs x)
    def get_x(self):
        return self.x
    
    # Accessor method for y (outputs y)
    def get_y(self):
        return self.y


# creating an object of the Point2D Class (__init__) initializer
point1 = Point2d(4,10)
point2 = Point2d(5,9)


# Return a string representation of this object (__str__)
# print(point1)
# print(point2) 

    
# Adds this object to another object from the same class, return a new object. (__add__)
# print(point1 + point2)

   
# Subtracts another object from this object, return a new object. (__sub__)
# print(point1 - point2)


# Test equality between this object and another, return a boolean. (__eq__)
point3 = Point2d(3,4)  
point4 = Point2d(3,4)
# print(point3 == point4)

# less than function (__lt__)
point5 = Point2d(10,12) 
point6 = Point2d(5,15)
# print(point5 < point6)
    
# Mutator method  
point7 = Point2d(5,11) # (set_x) our method will change the value of x
point7.set_x(10)
# print(point7)

point7.set_y(25) # (set_y) our method will change the value of y
# print(point7)

# Accessor method 
# print(point7.get_x())  # (get_x) outputs x
# print(point7.get_y())  # (get_y) outputs y


"""" Exercise - Dog Class
This class will take 3 parameters, dog name, dog breed, and age (human years)"""

class Dog:

    def __init__(self, name, birth_year, breed):
        self.name = name
        self.birth_year = birth_year
        self.breed = breed
    
    def __str__(self):
        return f"{self.name} is a {self.breed} who was born in {self.birth_year}"
        
    def human_age(self):
        today = datetime.datetime.now()
        year = today.year
        return year - self.birth_year
    
    # Write a method that will calculate dog years
    # Long version
    # def dog_years(self):
    #     today = datetime.datetime.now()
    #     year = today.year
    #     return f"{self.name} is {(year - self.birth_year) * 7} years old in dog years"
    
    # Short version
    def dog_years(self):
        dog_years =  7 * self.human_age()
        return f"{self.name} is {dog_years} in dog years"
       

dog1 = Dog("Fido", 2020, "Golden Retriver") # Created our first object of the dog class
dog2 = Dog("Zuzu", 2021, "Dachsund")
dog3 = Dog("Stella", 2016, "Japanese Chin")

# String Representation
# print(dog1)
# print(dog2)
# print(dog3)

# Human Age Method
# print(dog1.human_age())
# print(dog2.human_age())
# print(dog3.human_age())

# Dog Years Method
# print(dog1.dog_years())
# print(dog2.dog_years())
# print(dog3.dog_years())

# today = datetime.datetime.now()
# year = today.year
# print(year)

     



''' Exercise - Date Class 

1. Display the date in a format of mm//dd/yyyy
2. compare 2 differenr dates, if they are equal
3. Compare which date came first
4. Determine if a date is a leap year
'''

class Date:

     def __init__(self, year=1970, month=1, day=1):
         """ These are our parameters"""
         self.year = year
         self.month = month
         self.day = day

     # this will control what the print built in function displays
     def __str__(self):
         return f"Month: {self.month:02d}\nDay: {self.day:02d}\nYear: {self.year}"
     
     # this will control what == does in your class
     def __eq__(self, other):
         if self.year == other.year and self.month == other.month and self.day == other.day:
             return True
         return False
     
     # create a method to handle less than date objects, which date came first
     def __lt__(self, other):
         selfdate = datetime.datetime(self.year, self.month, self.day)
         otherdate = datetime.datetime(other.year, other.month, other.day)
         if selfdate < otherdate:
             return True
         return False
     
     def is_leap_year(self):
         if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0):
            return True
         return False
    
my_date_info = Date(2004, 10, 4) # create the object
second_date = Date(2004, 10, 4)
default_date = Date(2005)
# print(default_date)

# String Representation
# print(my_date_info)

# Equality
# print(my_date_info == second_date)
 
old_date = Date(1998, 2, 10)
new_date = Date(2000, 2, 10)

# print(old_date < new_date)

my_new_date = Date(2008, 6, 1)
print(my_new_date.is_leap_year())

'''
Exercise - Dog Class
'''






