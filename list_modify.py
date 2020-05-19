motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[:])
print("\n")

# Modifying element in list
motorcycles[0] = 'ducati' # change the first list value to ducati
print(motorcycles)
print("\n")

# Append element to a list
motorcycles.append('tesla') # Append a single element to the end of the list
print(motorcycles)
print("\n")

# Inserting element to a list
motorcycles.insert(0, 'viar')
print(motorcycles)
print("\n")

# Removing element to a list
del motorcycles[0]
print(motorcycles)
print("\n")

# Removing an item Using the pop() Method
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
print(motorcycles)
print("\n")

# Popping items from any Position in a list
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")
print(motorcycles)
print("\n")


# Removing an item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
print("\n")

too_cheap = 'suzuki'
motorcycles.remove(too_cheap)
print(motorcycles)
print("A " + too_cheap.title() + " is too cheap for me.")
