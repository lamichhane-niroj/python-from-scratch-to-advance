# A function is said to be higher order function if it either
#                                                           -accept a function as an argument
#                                                           -returns a function 

def say_loud(text):
    return text.upper()


def say_soft(text):
    return text.lower()


# It is higher order function because it accepts function as an argument
def hello(func):
    text = func('Hello')
    print(text)


# print(say_loud('Hello'))
# print(say_soft('Hello'))

hello(say_loud)
hello(say_soft)


# It is also higher order function as it returns a function
def divisor(x):
    def divident(y):
        return y/x
    return divident


# new = divisor(5)
# value = new(5)
value = divisor(2)(10)
print(value)


