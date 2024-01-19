#string method

my_str = '   Hello world    '
greet = 'How are you?'
fruits = 'apple,banana,mango,grape,cherry'
Name = 'James'

#concatenation of string using * operator - prints n times the name
print(Name*3)                

#formatting string- %, .format and f-String
# % method, Its like C programming %d for integers, %f for float, %s for string
var = 'Tommy'
pie = 3.1415926
print('Hello %s' %var)
print('The value of pie is %.3f'%pie)

# .format method
print('Hello {}'.format(var))
print('The value of pie is {:.2}'.format(pie))

# f string method
print(f'Hello {var}')
print(f'The value of pie is {pie}')

# strip method - It returns the string with removing white front and back whitespaces
print(my_str.strip())

# lstrip method - It returns the string with removing left white spaces
print(my_str.lstrip())

# rstrip method - it returns the string with removing right white spaces
print(my_str.rstrip())

# upper method - It returns the string with all uppercase character
print(my_str.upper())

# lower method - It returns the string with all lowercase character
print(my_str.lower())

# startswith method - It returns true if string starts with given character or substring else false
print(my_str.startswith('   He'))

# endswith method - It returns true if string ends with given character or substring else false
print(my_str.endswith('    '))

# find method - It returns the index of the first find character or substring if present else returns -1
print(my_str.find('H'))

# rfind method - it returns the index from the right side
print("Hello".rfind('r'))

# count method - It returns the no of repeated character or substring
print(my_str.count('l'))

# replace method - It returns a new string replacing the substring with the given substring
print(my_str.replace('world','Universe'))

# split method - It returns a list by converting the string into list, default is whitespace so it seperates inorder to whitespaces
print(greet.split())
print(fruits.split(","))

# rsplit method - it returns a list by the right
print("h e l l o".rsplit(" "))

# splitlines - it splits each line
print('''How
are
you
doing?'''.splitlines())


# partition - it partition the whole string by the given string
print("Hello how are you?".partition("how"))

# rpartition - it partition the whole string by the given string to the right
print("Hello how are you?".partition("how"))

# join method - It is opposite of split, it converts list into the string
new_str = ''.join(greet)
print(new_str)

# capitalize method - It capatalize the first character
print(fruits.capitalize())

# isdigit method - It returns true if all character are digit else false
print(my_str.isdigit())     

# isalpha method - It returns true if there is only alphabets else false
alphabet = 'ABCDEF'
print(alphabet.isalpha())    

# islower - returns true or false
print(alphabet.lower().islower())

# isupper - returns true or false
print(alphabet.isupper())

# isnumeric, istitle, isspace, isdigit, isalpha, isalnum, isdecimal, isprintable, isidentifier

# ljust - It stick the string to left and fill the given width with the fillchar
print(alphabet.ljust(20, 'a'))

# lstrip - removes white space occurs in left
print(alphabet.lstrip())

# zfill - fill with zero to and center the alignment
print(alphabet.zfill(20))

# title - returns titlecase, first letter of each word is uppercase
title = 'i am learning python'
print(title.title())

# swapcase - converts lower to upper and upper to lower
print(title.swapcase())

# center - It centers the text with the given width and fill the extra space with fillchar
print(alphabet.center(20,'b'))

# encode - It encodes the string
enc = alphabet.encode('UTF-8', 'strict')
print(enc)

# decode - It decodes the string
print(enc.decode('UTF-8','strict'))

# it translates the ascii code
print("moonSan".translate({83: 80}))
