class Employ:
    #class variables
    company_name = 'DEF Company'

    #constructor to initialize the objects
    # (def :- constructor) (name, salary :- parameters to constructor)
    def __init__(self, name, salary):   # Attributes name and salary
        #instance varibles(data members)
        self.name = name
        self.salary = salary
    
    #instance methods
    def show(self):
        print(f"Employ:  {self.name} {self.salary} {self.company_name}")

# Creating the first object - obj1 is the first object of classs Employ
obj1 = Employ("Qasim", 19000)
obj1.show()

# Creating the second object - obj2 is the second object of classs Employ
obj2 = Employ("Wahab", 20000)
obj2.show()