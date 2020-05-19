# A list in a dictionary 1
# Store information about pizza being oredered
pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheese']
}

# Summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

print("\n")


# A list in a dictionary 2
favorite_languages = {
    'jen' : ['python', 'ruby'],
    'sarah' : ['c'],
    'edward' : ['ruby', 'go'],
    'phil' : ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print("\n" + name.title() + "'s favorite languages is:")
    else:
        print("\n" + name.title() + "'s favorite languages are:")
        
    for language in languages:
        print("\t" + language.title())