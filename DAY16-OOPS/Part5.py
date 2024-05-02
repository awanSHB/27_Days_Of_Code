#Multiple constructor

class Vehicle:

    def __init__(self, engine):
        print("inside the 1st construtor")
        self.engine = engine

class Car(Vehicle):
    def __init__(self, engine, max_speed):
        super().__init__(engine)
        print("Inside the 2nd constructor")
        self.max_speed = max_speed
    
class Electric_Car(Car):
    def __init__(self, engine, max_speed, km_range):
        super().__init__(engine, max_speed)
        print("Inside the 3rd constructor")
        self.km_range = km_range
    
object_of_electric_car = Electric_Car('1500cc', 600, 900)

print(f'''Engine: {object_of_electric_car.engine}, max_speed: {object_of_electric_car.max_speed},km_range: {object_of_electric_car.km_range}''')