# The Car class

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Default value for an attribute

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statment showing the car's kilometer."""
        print("This car has " + str(self.odometer_reading) + " kilometers on it.")

    # Modifying an attribute's value through a method
    def update_odometer(self, km):
        """
        Set the odometer reading to the given value
        Reject the chang if it attempts to roll the odometer back
        """
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("You can't roll back an odometer!")

    # Incrementing an attribute's value through a method
    def increment_odometer(self, km):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += km
    
# New Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer() # You don't have to include parameter for default value

# Modifying an attribute's value directly
# my_new_car.odometer_reading = 200
# my_new_car.read_odometer()

# Modifying an attribute's value through a method
my_new_car.update_odometer(2)
my_new_car.read_odometer()
my_new_car.update_odometer(1)
print("\n")


# Used car
my_used_car = Car('toyota', 'rush', 2007)
print(my_used_car.get_descriptive_name())
my_used_car.increment_odometer(68000)
my_used_car.read_odometer()
my_used_car.increment_odometer(1000)
my_used_car.read_odometer()