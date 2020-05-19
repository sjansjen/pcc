# The Car class
class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's kilometers"""
        print("This car has " + str(self.odometer_reading) + " kilometers on it.")

    def update_odometer(self, km):
        """
        Set the odometer reading to the given calue.
        Reject the change if it attempts to roll the odometer back.
        """
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, km):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += km
    
    
class Battery():
    """A simple attempt to model a battery for an electric car"""
    def __init__(self, battery_size = 70):
        """Initialize the battery's attribute"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provide."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go appoximately " + str(range)
        message += " kilometers on a full charge."
        print(message)


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then Initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()