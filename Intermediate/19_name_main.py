# python interpreter sets special variable, one of which is __name__, python will assign this value to 'main' for the initial module

def greet():
    print('Hello world')


print(__name__)

if __name__ == "__main__":
    greet()

