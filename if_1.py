# Simple IF
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print("\n")



# Checking for inequality
requested_topping = 'mushrooms'

if requested_topping != 'anchoives':
    print("Hold the anchoives!")
print("\n")



# Numerical Comparisons
answer = 17

if answer != 42:
    print("That is not the corerct answer. Please try again!")
print("\n")


# Checking whether a value is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
else:
    print(user.title() + ", you can't post a response.")
