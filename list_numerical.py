# Using range() function to generate a series of numbers
for value in range(1,5):
	print(value)


# Using range() to make a list of numbers
numbers = list(range(1,5))
print(numbers)

even_number = list(range(2,10,2))
print(even_number)

squares = []
for value in range(1,11):
	squares.append(value ** 2)

print(squares)

# Simple statistics with a list of numbers
print(min(squares))
print(max(squares))
print(sum(squares))
print("\n")


# List Comprehensions, generate list in just one line of code
squares = [value**2 for value in range(1,11)]
print(squares)
