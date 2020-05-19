# Tuple = a list of items that cannot change
dimensions = (200, 50) # Tuple use parentheses(), not square bracket []
print(dimensions[0])
print(dimensions[1])
print('\n')

# Python will give an error if you try to change value in Tuple
# dimensions[0] = 100


# Looping through all value in a Tuple
for dimension in dimensions:
	print(dimension)
print('\n')


# Writing over a Tuple
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)
	
dimensions = (400, 100)
print("\nModified dimension")
for dimension in dimensions:
	print(dimension)
