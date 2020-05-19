# Reading entire file
with open('pi_digits.txt') as file_object: # 'pi_digits.txt can be replace by file path
    contents = file_object.read()
    print(contents)



# Reading line by line
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())



# Making a list of lines from a file
with open(file_name) as file_object:
    # readlines() method takes each line from file and stores it in a list
    lines = file_object.readlines() 

for line in lines:
    print(line.rstrip())



# Working with a file's contents
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))



# Large files: One million digits
file_name_2 = 'pi_million_digits.txt'
with open(file_name_2) as file_object_2:
    lines = file_object_2.readlines()

pi_string_million = ''
for line in lines:
    pi_string_million += line.strip()

print(pi_string_million[:50] + "...")
print(len(pi_string_million))