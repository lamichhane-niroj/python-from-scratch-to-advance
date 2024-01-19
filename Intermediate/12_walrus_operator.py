# walrus operator :=
# It is new to python 3.8
# Assignment with expression
# assign value to the variable of a larger expression

# we can write
var = 'Hello'
print(var)
# print(var = 'Hello') #This is not allowed

# using walrus operator
print(var := 'Hello')  # But this is allowed

# with normal codes
foods = []
while True:
    food = input('Enter the food: ')

    if food == 'q' or food == 'Q':
        break
    foods.append(food)

# with walrus operator
Foods = []
while (food := input('Enter the food: ')) != 'q':
    Foods.append(food)

print(Foods)
