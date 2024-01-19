#for taking user inputs we use input function

a = input("Enter a number ") #takes input and stores to a(variable)
print(a)

#lets check the type of a
print(type(a))

#oops it's of string class i.e input function receives input in the form of string
b = 10

# c = a+b 
#This will throw an error as we are adding string and number which doesn't make sense
#we need to type-cast it
a = int(a)
c = a+b   #now works properly
print(c)

