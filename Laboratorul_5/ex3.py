class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, seats):
        super().__init__(make, model, year)
        self.seats = seats

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_type):
        super().__init__(make, model, year)
        self.engine_type = engine_type

class Truck(Vehicle):
    def __init__(self, make, model, year, cargo_capacity):
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity

    def calculate_towing_capacity(self):
        return self.cargo_capacity * 0.8

# Example usage

car = Car("Honda", "Accord", 2023, 5)
print(f"Car details: {car.make} {car.model} ({car.year}), {car.doors} doors")

motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2022, "V-twin")
print(f"Motorcycle details: {motorcycle.make} {motorcycle.model} ({motorcycle.year}), Engine type: {motorcycle.engine_type}")

truck = Truck("Ford", "F-150", 2020, 8000)
print(f"Truck details: {truck.make} {truck.model} ({truck.year}), Towing capacity: {truck.calculate_towing_capacity()} lbs")