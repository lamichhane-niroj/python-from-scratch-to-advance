# tuple are the similar to list but immutable elements
# immutable, ordered, duplicate set of data

Ocean = ("Pacific", "Indian", "Atlantic", "Artic", "Southern")
print(Ocean)
# Ocean[0] = 1 #This will generate error

print(Ocean[2])

tu = (1,) #tuple with single element
tu1 = ()  #empty tuple

tu2 = (1) # this is not the way to create tuple with one element

print(tu, tu1,type(tu2)) 
