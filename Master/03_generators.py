# A generator is a simplest way to create iterator
# A generator-function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword
# rather than return. 
# If the body of a def contains yield, the function automatically becomes a generator function. 

# creating our own range function
class Iter:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        self.current += 1
        if self.current >= self.n:
            raise StopIteration
        return self.current


x = Iter(10)

for i in x:
    print(i)


# above job can be done using generator in simple way
def gen(n):
    for i in range(n):
        yield i


# Why to use generator
import sys

L = [x for x in range(1000000)]

#for i in L:
    #print(i**2)

print(sys.getsizeof(L))

x = range(100000000)

#for i in x:
    #print(i**2)
print(sys.getsizeof(x))


# generator function
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
  
def simplefunc():
    return 1,2,3,4,5


print(sys.getsizeof(simplefunc))
print(sys.getsizeof(simpleGeneratorFun))

for value in simplefunc():
    print(value)

for value in simpleGeneratorFun():
    print(value)
    

# generator function returns an iterator
x = simpleGeneratorFun()

# Iterating over the generator object using next
print(next(x)) # In Python 3, __next__()
print(next(x))
print(next(x))






