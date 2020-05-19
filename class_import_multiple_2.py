# Import a module into a module
# See electric car.py

from car_2 import Car
from electric_car import ElectricCar

my_bettle = Car('volkswage', 'beetle', 2016)
print(my_bettle.get_descriptive_name())

my_tesla = ElectricCar('telsa', 'model y', 2018)
print(my_tesla.get_descriptive_name())