cars = ['bmw', 'audi', 'toyota', 'subaru']

# Permanently sort in alphabetical order
cars.sort()
print(cars)

# Permanently sort in reverse alphabetical order
cars.sort(reverse = True)
print(cars)


# Temporarily sort in alphabetical order
print("\nHere is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the reverse sorted list:")
print(sorted(cars, reverse = True))
print("\nHere is the original list again:")
print(cars)
print("\n")


# Printing a list in reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

# Find the length of a list
print(len(cars))
