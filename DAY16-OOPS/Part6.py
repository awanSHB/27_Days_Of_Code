class Employe:

    def __init__(self, name, age):
        #:- Data Members/Instance variables
        #:- Public Member
        self.name = name

        #:- Private Member
        self._age = age

    # Accessing the Private member with the help of instance method/public instance method
    def show(self):
        print(f"Name : {self.name} Age : {self._age}")
    
emp = Employe('Amir', 20)

emp.show()