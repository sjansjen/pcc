magicians = ['alice', 'david', 'carolina']

# for loop, pull an name from the list magicians and store it in variable magician
for magician in magicians: 
	print(magician)

print('\n')

for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")


# doing something after loop
print("Thank you, everyone. That was a great magic show!")
