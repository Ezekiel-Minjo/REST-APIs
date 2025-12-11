class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year

    def info(self):
        return f"{self.year} {self.make}"
    
    @classmethod
    def future_model(cls, car):
        return cls(car.make, car.year + 1)
    
    @staticmethod
    def car_summary(car):
        return f"Make: {car.make}, Year: {car.year}"
    
c1 = Car("Toyota", 2025)
c2 = Car.future_model(c1)

print(c2.info())    
print(Car.car_summary(c1)) 
