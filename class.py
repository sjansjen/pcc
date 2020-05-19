# Create a Class

class Dog():
    """ A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        """Simulate roling over in response to a command."""
        print(self.name.title() + " rolled over!")


# Making multiple instances from a class
my_dog = Dog('opi', 10)
your_dog = Dog('tucker', 7)


# Calling Methods
print("My dog name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()

print("\nYour dog name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")

your_dog.sit()
your_dog.roll_over()