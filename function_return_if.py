# Returning a simple value

def get_formatted_name_1(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name_1('jimi', 'hendrix')
print(musician)



# Making an argument optional

def get_formatted_name_2(first_name, last_name, middle_name = ''):
    """Return a full name, neatly formatted."""
    if middle_name: # Python interperts non-empty strings as True
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name_2('jimi', 'hendrix')
print(musician)

musician = get_formatted_name_2('john', 'hooker', 'lee')
print(musician)



# Returning a dictionary

def build_person(first_name, last_name, age = ''):
    """Return a dictionary of information about a person."""
    person = {'first' : first_name, 'last' : last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)