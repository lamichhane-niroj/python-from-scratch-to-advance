# Python has a built-in module that you can use to make random numbers.
import random

# random.random -> generates a float number in interval [0,1]
print(random.random())

# random.uniform -> Returns a random float number between two given parameters
print(random.uniform(10.5, 15.5))

# random.sample -> Returns a given sample of a sequence
fruits = ['apple', 'banana', 'cherry']
print(random.sample(fruits, k=2))

# random.randint -> returns an integer of the given inclusive range
print(random.randint(1, 6))

# random.randrange -> Returns a random number between the given exclusive range 
print(random.randrange(1, 6))

# random.choice -> Returns a random element from the given sequence
lst = ['Rock', 'Paper', 'Scissors']
print(random.choice(lst))

# random.choices ->Returns a list with a random selection from the given sequence
print(random.choices(lst, k=10, weights=[10, 10, 2]))

# random.suffle -> Takes a sequence and returns the sequence in a random order
random.shuffle(lst)
print(lst)

# getstate and setstate method
state = random.getstate()
print(random.random())

print(random.random())
print(random.random())

random.setstate(state)
print(random.random())

# getrandbits method -> Returns a number representing the random bits
print(random.getrandbits(3))

# seed function - it helps to generate same random number everytime
random.seed(10)
print(random.random())

random.seed(10)
print(random.random())

# triangular function - it helps to generate a floating number between given range both inclusive
print(random.triangular(10, 20))
