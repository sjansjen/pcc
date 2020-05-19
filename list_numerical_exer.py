#for numbers in range(1,21):
	#print(numbers)

numbers = list(range(1,1000001))
#print(numbers)

print(min(numbers))
print(max(numbers))
print(sum(numbers))


for odd_numbers in range(1,21,2):
	print(odd_numbers)

threes = [value*3 for value in range(3,31)]
print(threes)

cubes = [r**3 for r in range(1,11)]
print(cubes)
