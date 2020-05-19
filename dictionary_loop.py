# Looping through all key-value pairs
user_0 = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi'
    }

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)



favorite_languages = {
    'jen' : 'python', 
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
    }
print("\n")

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")


print("\n")


# Looping through all keys
friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("  Hi " + name.title() + ", I see your favorite language is " +
        favorite_languages[name].title() + '!')


print("\n")


# Looping through dictionary keys in order
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")


print("\n")


# Looping through all values in a dictionary
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
print("\n")

# To remove repeated values, use set()
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())