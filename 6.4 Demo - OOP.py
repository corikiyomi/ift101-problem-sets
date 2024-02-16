# Object Oriented Programming Demonstration

class Car():
    # A simple attempt to represent a car
    def __init__(self, make, model, year):
        # Initialize attribute to describe the car
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        # Return a neatly formatted descriptive name
        description = f'{self.year} {self.make} {self.model}'
        return description.title()
    
    def read_odometer(self):
        # Print a statement showing the car's mileage
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        # Set the odometer reading to the given value
        # Reject the change if it attempts to roll back the odometer value
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back an odometer!')
        
    def drive(self, miles):
        # Add the given amount of miles driven to the odometer reading
        if miles >= 0:
            self.odometer_reading += miles
        else: 
            print('You must drive 0 or more miles!')

    def fill_gas_tank(self):
        # Fills the gas tank
        print('The tank is now full.')

    def press_horn(self):
        print('Beep! Beep!')

# Creating an instance from a class: Car
# The class definition is the blueprint or instructions for creating a car object
my_car = Car('mazda', 'mazda6', 2015)
print(my_car.get_descriptive_name())

my_car.read_odometer()
my_car.update_odometer(50)
my_car.read_odometer()
my_car.drive(50)
my_car.read_odometer()
my_car.fill_gas_tank()
my_car.press_horn()

# Inheritance
# Use inheritance to create another object — an Electric Car
class ElectricCar(Car):
    # Represent aspects of a car, specific to electric vehicles
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_capacity = 70

    def describe_battery(self):
        # Print a statement describing the battery capacity
        print(f'This car has a {self.battery_capacity}-kWh battery.')
    
    def fill_gas_tank(self):
        # Override the fill_gas_tank() method from Car class
        print('The batter is now fully charged!')

    def press_horn(self):
        print('Cha-ching!')

my_jeep = ElectricCar('jeep', 'wrangler 4xe', 2023)
print(my_jeep.get_descriptive_name())
my_jeep.read_odometer()
my_jeep.describe_battery()
my_jeep.drive(200)
my_jeep.read_odometer()
my_jeep.fill_gas_tank()
