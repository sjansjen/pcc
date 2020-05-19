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
