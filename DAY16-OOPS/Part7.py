# Base class
class Company:
    def __init__(self):
        #Protected member
        self.project = "NLP"

#Child Class    
class Employ:
    def __init__(self, name) -> None:
        self.name = name
        Company.__init__(self)
    
    def show(self):
        print(f"name is : {self.name}")
        #Accessing the protected member in Child class
        print(f"Working on the project : {self.project}")
    
emp = Employ("Jess")
emp.show()