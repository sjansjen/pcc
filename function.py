# Function
def greet_user(username): # Funtion definition
    """Display a simple greeting.""" # Docstring, a comment which describes what the function does
    print("Hello " + username.title() + "!") # The actual code

greet_user('jesse')



# Passing Arguments

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry') ## Positional Arguments
describe_pet('dog', 'willie') ## Positional Arguments

describe_pet(pet_name='harry', animal_type='hamster') ## Keyword Arguments
