# A decorator function is a function that accepts a function as parameter, modifies it and returns a function
def check_score(func):
    print("Scores checked")

    def update_score():
        print("Scores updated")
        func()
    return update_score

@check_score
def set_high_score():
    print("Highscore set")



# To avoid below line we will be using decorators
# set_high_score = check_score(set_high_score)


set_high_score()


# suppose you have a function that returns the addition of two values, you need to get the addition of 3 values
# you cannot modify the old function because you have imported it so how to solve this problem?

def decor(func):
    def inner():
        z = float(input("Enter third number: "))
        res = func()
        return res + z
    return inner

@decor
def addition():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    return x+y


# addition = decor(addition)

print(addition())
