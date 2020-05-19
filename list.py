bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0]) # [0] pull the first list
print(bicycles[0].title())
print(bicycles[2])
print(bicycles[3])

print(bicycles[-1]) # [-1] pull the last element in a list
print(bicycles[-2]) # [-2] pull the last second element in a list

message = ("My first bicycle was a " + bicycles[0].title() + ".")
print(message)
