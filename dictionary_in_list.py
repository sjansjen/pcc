# A List of dictionaries
alien_0 = {'color' : 'green', 'points' : 5}
alien_1 = {'color' : 'yellow', 'points' : 10}
alien_2 = {'color' : 'red', 'points' : 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
print('...')


# Make a list of dictionaries automaticly using range()
# Empty list for storing aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green' :
        alien['color'] = 'yellow'
        alien['speed'] = 'meddium'
        alien['points'] = 10
        
# Show the firs 5 aliens:
for alien in aliens [:5]:
    print(alien)
print('...')

# Show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))