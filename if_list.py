# Checking for special items

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of " + requested_topping + " right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!\n")


# Checking that a list is no empty
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?\n")



# Using multiple lists
available_toppings1 = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings1 = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping1 in requested_toppings1:
    if requested_topping1 in available_toppings1:
        print("Adding " + requested_topping1 + ".")
    else:
        print("Sorry, dont have " + requested_topping1)

print("\nFinishied making your pizza!")