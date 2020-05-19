# Passing an arbitrary number of arguments

def make_pizza_1(*toppings): # * to make empty Tuple
    """Summarize the pizza we are about to make"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza_1('pepperoni')
make_pizza_1('mushrooms', 'green perppers', 'extra cheese')



# Mixing positional and arbitrary arguments

def make_pizza_2(size, *toppings): # The *Tuple parameter must be placed last
    """Summarize the pizza we are about to make"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza_2(16, 'pepperoni')
make_pizza_2(12, 'mushrooms', 'green perppers', 'extra cheese')



# Using arbitrary keyword arguments

print("\n")
def build_profile(first, last, **user_info): # ** To create an empty dictionary and pack name-value pairs
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

print(user_profile)