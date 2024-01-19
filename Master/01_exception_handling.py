# exception is a runtime error which can be handled by programmer. All exception belong to their class in python
# exception handling helps to make program user friendly and program won't terminate after exception or error is occurred

# simple exception handling
# division by zero exception

# try block throws the exception to except block whenever exception occurs and except block catches the exception
while True:
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    try:
        div = a/b
        print('The division is',div)
    except ZeroDivisionError:
        print('The divider must not be zero')

    if var:=input('Press q to quit:') == 'q':
        break


# try - except with else - else will execute whenever try statement will execute
# handling nameerror exception

try:
    a = 10
    print('The value of a*b is', a*d)  # here d is not defined which raises exception
except NameError as ne:
    print(ne)   # These exception contains itself some message...
else:
    print('I make sure that try block executes')


# try - except with finally - finally will execute irrespective execution of try or except block
try:
    print('Hello python learners') 
except NameError as ne:
    print(ne)   # These exception contains itself some message...
else:
    print('I make sure that try block executes')
finally:
    print('I have nothing to do with try or except or else block')


# try block with multiple exception blocks
try:
    a = 20
    b = 0
    print('The division is', a/b)
except NameError as ne:
    print(ne)
except ZeroDivisionError as zd:
    print(zd)


# multiple exception block with tuple
try:
    a = 20
    b = 0
    prin('The division is',a/b)
except (NameError,SyntaxError,ZeroDivisionError):
    print('ALERT ////Exception occured!!')


# handling any kind of exception
try:
    a = 5
    b = 0
    print('a/b=', a/b)
except:
    print('ALERT ////Exception occured!!')



