players = ['charles', 'martina', 'michael', 'florence', 'eli']

# Slicing a list : pull elements from any point of a list
print(players)
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print("\n")

# Looping through a slice
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())
print("\n")

# Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # ([:]) Copy a new list from a slice

my_foods.append('ice cream')
friend_foods.append('cannoli')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend favorite foods are:")
print(friend_foods)
