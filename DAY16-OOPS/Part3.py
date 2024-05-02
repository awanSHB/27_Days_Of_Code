print('---Encapsulation---')

class Employee:
    def __init__(self, name, salary):
        #public member
        self.name = name
        
        #private member
        #not accessable from outside the class
        self.__salary = salary

    def show(self):
        print(f"Name: {self.name} {self.__salary}")

o1 = Employee("ABCD", 20000)
o1.show()

print(o1.__salary)  #unaccessabel from outside the class