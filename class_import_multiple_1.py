# Import multiple classes from a module
from car_1 import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2022)
print(my_tesla.get_descriptive_name())



# Import an entire module
import car_1

my_beetle = car_1.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car_1.ElectricCar('tesla', 'roadster', 2022)
print(my_tesla.get_descriptive_name())



# Import all classes from a module
# from car_1 import *