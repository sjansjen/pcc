alien_0 = {'color' : 'green', 'points' : 5}

# Accessing values in a dictionary
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!\n")


# Adding new key - value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


# Starting with an empty dictionary
print("\n")

alien_1 = {}
alien_1['color'] = 'blue'
alien_1['points'] = '10'
print(alien_1)

# Modifying values in a dictionary
print("\n")
alien_1['color'] = 'red'
print(alien_1)

## Move the alien to the right
## Determine how far to move the alien based on its current speed.
print("\n")

alien_2 = {'x_position' : 0 , 'y_position' : 25, 'speed' : 'medium'}
print("Original x-position: " + str(alien_2['x_position']))

if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

##The new position is the old position plus the increment
alien_2['x_position'] = alien_2['x_position'] + x_increment

print("New x-position: " + str(alien_2['x_position']) + "\n")


# Removing key-value pairs
print(alien_2)
del alien_2['speed']
print(alien_2)