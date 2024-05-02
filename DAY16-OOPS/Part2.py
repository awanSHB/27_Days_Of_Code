from unicodedata import name


class Student:
    #constructor
    def __init__(self, name, marks):
        #instance variables
        self.name = name
        self.marks = marks

# Creating the first object
obj1 = Student("Abc", 80)

#Accessing the instance variable
print("OBJECT 1")
print("Name: ", obj1.name)
print("Marks: ", obj1.marks)
print()
# Creating the second objects
obj2 = Student("DEF", 90)

#Accessing the instance varibles
print("OBJECT 2")
print("Name: ", obj2.name)
print("Marks: ", obj2.marks)