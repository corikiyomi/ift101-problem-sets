# Car Dealership
    # inheritance, polymorphism in OOP

import datetime as dt

# Create a class Vehicle
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f'Vehicle:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}\nAge: {self.get_age()}\n')

    def get_age(self):
        # Use datetime as dt to get current year
        today = dt.date.today()
        current_year = today.year
        self.age = current_year - self.year
        return f'{self.age} years old'

# Create a class Truck, inherit Vehicle, add max_load     
class Truck(Vehicle):
    def __init__(self, make, model, year, max_load):
        super().__init__(make, model, year)
        self.max_load = max_load

    def display_info(self):
        print(f'Vehicle:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}\nAge: {self.get_age()}\nMax Load: {self.max_load} lbs\n')

    def can_carry(self, weight):
        if self.max_load >= weight:
            print(f'Can the truck carry {weight}? Yes\n')
        else:
            print(f'Can the truck carry {weight}? No\n')

# Instantiate Vehicle object(s)
mazda6 = Vehicle('Mazda', 'Mazda6', 2015)
mazda6.display_info()
mazda6.get_age()

tesla = Vehicle('Tesla', 'Model 3', 2022)
tesla.display_info()
tesla.get_age()

# Instantiate Truck object(s)
wrangler = Truck('Jeep', 'Wrangler 4xe', 2023, 3300)
wrangler.display_info()
wrangler.get_age()
wrangler.can_carry(11000)
        
f150 = Truck('Ford', 'F-150', 2020, 10000)
f150.display_info()
f150.get_age()
f150.can_carry(11000)
        