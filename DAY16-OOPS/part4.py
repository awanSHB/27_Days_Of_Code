class Company:
    #unparametrized constructor
    def __init__(self):
        #instance variables(Data members)
        self.name = 'ABC'
        self.address = "XYZ Street"

    #a method(an instance method) for printing the data members
    def show(self):
        print(f"The name is : {self.name} and the address is {self.address}")
    
#Creating the object of the class
com = Company()

#calling the object using the instance method
com.show()