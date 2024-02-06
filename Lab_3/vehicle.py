#Define a base class, e.g., Vehicle, with attributes such as make, model, and year.
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

    def __add__(self, other):
        return f"{self.make} {self.model} + {other.make} {other.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors, fuel_type):
        super().__init__(make, model, year)
        self.num_doors = num_doors
        self.fuel_type = fuel_type

vehicle1 = Vehicle('Honda', 'Accord', 2020)
vehicle2 = Vehicle('Ford', 'Escape', 2021)
car1 = Car('Toyota', 'Corolla', 2022, 4, 'Gasoline')

vehicle1.display_info()
vehicle2.display_info()
car1.display_info()

result = vehicle1 + vehicle2
print("Concatenation result:", result)
