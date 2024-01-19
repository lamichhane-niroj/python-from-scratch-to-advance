# args are argument given to the function,method, we can use *args for sequence of arguments

def add(*args):
    print(type(args))
    total = sum(args)
    return total


total = add(1, 2, 3, 4,  5)
print(total)


# kwargs are keyword argument given to the function,method, we can use **kwargs for sequence of keyword argument
def say_hello(**kwargs):
    print(type(kwargs))
    # print('Hello '+ str(kwargs['name']) + ' ' + str(kwargs['last_name']) + ' ' + str(kwargs['bro']))
    print('Hello', end=" ")
    for words in kwargs.values():
        print(words, end=" ")


say_hello(name='Niroj', last_name='Lamichhane', bro='bro')
