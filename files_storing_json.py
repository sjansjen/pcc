import json

# Create a list of numbers and store it in .json file using json.dump
"""
numbers = [2, 3, 5, 7, 11, 13]

filename = "numbers.json"
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
"""


# Read .json files content using json.load
filename = "numbers.json"
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)